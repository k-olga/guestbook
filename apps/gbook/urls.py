#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from django.contrib import admin
from django.conf.urls import patterns, include, url
from gbook.views import main_page, list_users
from gbook.feeds import GuestbookRecords

#admin.autodiscover()

#url(/r'^admin/', include(admin.site.urls)),

urlpatterns = patterns('gbook.views', 
    url(r'^main_page/$', 'main_page', name='gb_main_page'),
    url(r'^list_users/$', 'list_users', name='list_users'),
    url(r'^user_posts/$', 'user_posts', name='user_posts'),
    url(r'^posts.xml$', 'xml_view', name='xml_view'),
    url(r'^feed/latest/$', GuestbookRecords(), name='rss_view'),
)
     