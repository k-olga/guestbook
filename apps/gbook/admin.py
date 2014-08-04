#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from gbook.models import GuestBookPost


admin.site.register(GuestBookPost, admin.ModelAdmin)
