# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
    url(r'^authenticate/(\?next=(?P<next_url>[\w/]+))?$', views.authenticate_view, name='authenticate'),
    url(r'^$', views.logout_view, name='logout'),
    )