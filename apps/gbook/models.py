#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime


class GuestBookPost(models.Model):
    name = models.CharField(max_length=45)
    text = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)
   
    def __unicode__(self):
        return u'%s' % self.name
                         