import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'login_site.settings'

if __name__ == '__main__':

    send_mail(
        '来自www.xxxxx.com的测试邮件',
        '欢迎访问www.xxxxx.com，这里是xx站点，本站专注于xx内容的分享！',
        '1205628156@qq.com',
        ['archimedes11@163.com'],
    )



