# -*- coding: utf-8 -*-

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^welcome',views.welcome),
    url(r'^login',views.login),
    url(r'^successful',views.successful),
    url(r'^signup',views.signup),
    url(r'^explore',views.explore),
]