from django.shortcuts import render, redirect
from . import models
from . import forms
import hashlib
from django.conf import settings
import datetime
from django.utils import timezone
from login.models import MoviesInfo, UserMovies, User, UserRating, SensitiveWord,MoviesClassicInfo,MoviesNewestInfo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse, HttpResponseRedirect

MOVIE_TITLE = ''


def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user, )
    return code


def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives

    subject, from_email, to = '来自二向箔影视的邮件', '1205628156@qq.com', email
    text_content = '欢迎注册访问二向箔影视，这里是二向箔影视的站点，本站专注于电影资源的分享！'
    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>45.40.250.238/confirm/</a>，\
                    这里是二向箔影视的站点，本站专注于电影资源的分享！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('45.40.250.238', code, settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('done')


def hash_code(s, salt='mysite'):  # 加密
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def index(request):
    movies_list = MoviesInfo.objects.all()
    paginator = Paginator(movies_list, 12)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'login/e1hjid/2-movie/index.html', {'movies_info': contacts})


def guest(request):
    # uid = User.objects.get(name = request.session.get('user_name','')).id
    # movies_info = UserMovies.objects.filter(userid = uid)
    movies_info = UserMovies.objects.filter(userid=request.session.get('user_id', ''))
    paginator = Paginator(movies_info, 12)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'login/e1hjid/2-movie/guess.html', {'movies_info': contacts})


def newest(request):
    # uid = User.objects.get(name = request.session.get('user_name','')).id
    # movies_info = UserMovies.objects.filter(userid = uid)
    movies_list = MoviesNewestInfo.objects.all()
    paginator = Paginator(movies_list, 12)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'login/e1hjid/2-movie/newest.html', {'movies_info': contacts})


def classic(request):
    # uid = User.objects.get(name = request.session.get('user_name','')).id
    # movies_info = UserMovies.objects.filter(userid = uid)
    movies_list = MoviesClassicInfo.objects.all()
    paginator = Paginator(movies_list, 12)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'login/e1hjid/2-movie/classic.html', {'movies_info': contacts})


def get_titile(request):
    return request.session.get()


def play(request, title):
    movie_info = MoviesInfo.objects.filter(title=title)
    # ls = []
    # info = testcase_info.objects.get(id=db_id)
    # url = info.url
    # path_type = info.path_type.replace("'", "").strip("[]").strip().split(',')
    # sensitive_word = list(models.SensitiveWord.objects.values().values_list('sensitive_word'))
    # print("1:",type(sensitive_word))
    # my_list = []
    # for var in sensitive_word:
    #     var_new = str(var)
    #     my_list.append(var_new.replace(',','').replace("'",'').replace('(','').replace(')',''))
    # print(my_list[0])
    # my_list = []
    # for var in sensitive_word:
    #     var = str(var)
    #     my_list.append(var.replace(',',''))
    # sensitive_word = SensitiveWord.objects.values()
    # sensitive_word_list = sensitive_word.replace("'", "").strip("[]").strip().split(',')
    # for var in sensitive_word:
    #     sensitive_word_list.append(var)
    # print(list(sensitive_word))
    if title == 'holder.js/50x50':
        pass
    else:
        request.session['movie_title'] = title
    test = request.session.get('movie_title', '')
    # test = request.COOKIES["movie_title"]

    # print('3：'+test)
    rating_info = UserRating.objects.filter(title=title)
    # movie_views = Movies_views.objects.filter(title=title)
    return render(request, 'login/e1hjid/2-movie/play.html', {"movie_info": movie_info, 'rating_info': rating_info, })


def search(request):
    sreach_name = request.GET.get("title", "")
    # sreach_name_bytes = sreach_name.encode(encoding="utf-8")
    movie_info = MoviesInfo.objects.filter(title=sreach_name)
    rating_info = UserRating.objects.filter(title=sreach_name)
    return render(request, 'login/e1hjid/2-movie/play.html', {"movie_info": movie_info, 'rating_info': rating_info, })


def login(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if not user.has_confirmed:
                    message = "该用户还未通过邮件确认！"
                    return render(request, 'login/login.html', locals())
                if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['movie_title'] = ''
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def user_rating(request):
    user_name = request.session.get('user_name', '')
    user_id = request.session.get('user_id', '')
    movie_title = request.session.get('movie_title', '')

    span = request.POST.get('span', '')
    sensitive_word = SensitiveWord.objects.all()
    # print(sensitive_word)
    comment = request.POST.get('comment', '').replace('<p>', '').replace('</p>', '').replace('<br/>', '')

    sensitive_word = list(models.SensitiveWord.objects.values().values_list('sensitive_word'))
    sensitive_word.append('美国')
    # print("1:", type(sensitive_word))
    my_list = []
    for var in sensitive_word:
        var_new = str(var).replace(',', '').replace("'", '').replace('(', '').replace(')', '')
        comment = comment.replace(var_new,'*')
        # my_list.append(var_new.replace(',', '').replace("'", '').replace('(', '').replace(')', ''))
    # print(my_list[0])
    # print(comment)
    if comment == '':
        pass
    else:
        try:
            models.UserRating.objects.create(user_name=user_name, user_id=user_id, title=movie_title, span=span,
                                             comment=comment)
        except:
            print("错误")
    # print("2:",movie_title)
    rating_info = UserRating.objects.filter(title=movie_title)
    movie_info = MoviesInfo.objects.filter(title=movie_title)
    # movie_views = Movies_views.objects.filter(title=title)
    #return render(request, 'login/e1hjid/2-movie/play.html', {"movie_info": movie_info}, {"rating_info": rating_info})
    return render(request, 'login/e1hjid/2-movie/play.html', {"movie_info": movie_info, 'rating_info': rating_info, })
    # return redirect('/play/')


def user_info(request):
    userid = request.session.get('user_id', '')
    user = User.objects.filter(id=userid)
    return render(request, 'login/e1hjid/2-movie/user_info.html', {'user_info': user})


def register(request):
    # if request.session.get('is_login', None):
    #     # 登录状态不允许注册。你可以修改这条原则！
    #     return redirect("/index/")
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)

                message = '请前往注册邮箱，进行邮件确认！'
                return render(request, 'login/confirm.html', locals())  # 跳转到等待邮件确认页面。
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def change_password(request):
    user_name = request.session.get('user_name', '')
    password_new = hash_code(request.POST.get('password_new', ''))
    password_confirm = hash_code(request.POST.get('password_confirm', ''))
    password_old = hash_code(request.POST.get('password_old', ''))
    # password_old='9f325a7bd48ac08c58f2584f1e1d2cbfdb50f8187f2d032a34ade1df42d60ca5'
    passwd = None
    message = ''
    try:
        passwd = User.objects.get(name=user_name, password=password_old)
    except:
        message = "错误！"
    if not (passwd):
        message = "原始密码错误！"
        # return render(request,'login/e1hjid/2-movie/change_password.html',"原始密码错误！")
    elif password_new != password_confirm:
        message = "两次输入密码不一致！"
        # return render(request, 'login/e1hjid/2-movie/change_password.html', "两次输入密码不一致！")
    else:
        User.objects.filter(name=user_name, password=password_old).update(password=password_new)
        message = "修改成功"
        # return render(request, 'login/e1hjid/2-movie/change_password.html', "修改成功")
    return render(request, 'login/e1hjid/2-movie/change_password.html', {'message': message})


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")


def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time
    now = timezone.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'login/confirm.html', locals())
