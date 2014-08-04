#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from gbook.models import GuestBookPost

    
class GuestbookRecords(Feed):
    
    title = u'Записи в Guestbook'
    description = u'Последние записи Guestbook'
    
    def link(self):
        return reverse('gb_main_page')
        
    def items(self):
        return GuestBookPost.objects.all().order_by('-id')[:15]
        
    def item_description(self, item):
        item_text = '.'.join(item.text.split('.')[:1])
        return item_text
        
    def item_link(self, item):
        return reverse('gb_main_page')
                
    def item_guid(self, obj):
        pass    
          
    def item_author_name(self, item):
        return item.name
    
    def item_pubdate(self, item):
        return item.creation_date        