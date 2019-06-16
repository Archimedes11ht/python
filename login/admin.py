# login/admin.py

from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.User)
admin.site.register(models.ConfirmString)
admin.site.register(models.MoviesInfo)
admin.site.register(models.UserRating)
admin.site.register(models.UserMovies)