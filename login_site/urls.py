"""login_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import url
from django.contrib import admin
from login import views
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^captcha', include('captcha.urls')),
    url(r'^confirm/', views.user_confirm),
    url(r'^guess/', views.guest),
    url(r'^play/(.+)$', views.play),
    url(r'^search/', views.search),
    url(r'^newest/', views.newest),
    url(r'^classic/', views.classic),
    url(r'^user_info/', views.user_info),
    url(r'^change_password/', views.change_password),
    url(r'^user_rating/', views.user_rating),
]
