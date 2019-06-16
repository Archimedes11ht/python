from django.db import models


# Create your models here.

class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    id = models.AutoField
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MoviesInfo(models.Model):
    span = models.CharField(max_length=50)
    img = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    actors = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.CharField(max_length=8)
    country = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    grenre = models.CharField(max_length=50)

class MoviesClassicInfo(models.Model):
    span = models.CharField(max_length=50)
    img = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    actors = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.CharField(max_length=8)
    country = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    grenre = models.CharField(max_length=50)

class MoviesNewestInfo(models.Model):
    id = models.AutoField
    span = models.CharField(max_length=50)
    img = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    xq_urlname = models.CharField(max_length=100)



class UserMovies(models.Model):
    id = models.AutoField
    span = models.CharField(max_length=50)
    img = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    actors = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.CharField(max_length=8)
    country = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    grenre = models.CharField(max_length=50)
    userid = models.IntegerField()


class Meta:
    ordering = ["-c_time"]
    verbose_name = "用户"
    verbose_name_plural = "用户"


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code


class UserRating(models.Model):
    id = models.AutoField
    user_id = models.CharField(max_length=10)
    user_name = models.CharField(max_length=128)
    span = models.CharField(max_length=50)
    title = models.CharField(max_length=128)
    comment = models.CharField(max_length=400)

class SensitiveWord(models.Model):
    id = models.AutoField
    sensitive_word = models.CharField(max_length=50)


class Meta:
    ordering = ["-c_time"]
    verbose_name = "确认码"
    verbose_name_plural = "确认码"
