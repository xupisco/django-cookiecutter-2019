# coding: utf-8
from django.conf.urls import include, url

from . import views


app_name = 'core'
urlpatterns = [
    url(r'^$', views.home, name='home',),
    url(r'^set_language/(?P<lang_code>[\w-]+)$', views.set_language, name='set_language'),
]
