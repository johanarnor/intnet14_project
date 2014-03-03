# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from case import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
    )