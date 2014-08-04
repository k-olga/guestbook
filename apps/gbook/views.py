#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from urlparse import urlparse

from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader 

from gbook.forms import GuestBookForm
from gbook.models import GuestBookPost

       
# главная страница
def main_page(request):
    # paginator
    posts_list = GuestBookPost.objects.all().order_by('-id')
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)    
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    post_method = None
        
    if request.method == 'POST':
        form = GuestBookForm(request.POST, post_method)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            d = GuestBookPost(name=name, text=text)
            d.save()
            return HttpResponseRedirect('')           
    else:
        form = GuestBookForm()
        
    return render_to_response('gbook/list_posts.html', 
                              {'form':form, 
                               'posts': posts}, 
                              context_instance=RequestContext(request)) 


#последние записи в формате XML                                              
def xml_view(request):
    xml_rs = u'<?xml version="1.0" encoding="utf-8"?>'
    posts = GuestBookPost.objects.all().order_by('-id')[:15]
    absolute_uri = request.build_absolute_uri()
    protocol = urlparse(absolute_uri).scheme
    host = urlparse(absolute_uri).netloc
        
    xml_news = u'<?xml version="1.0" encoding="utf-8"?>'
    xml_rs += u'<posts_list>'
    xml_rs += u'<header>Последние записи Guestbook</header>'
    xml_rs += u'<link>%s://%s%s</link>' % (protocol, host, reverse('gb_main_page'))
            
    for post in posts:
        post_author = post.name
        post_date = post.creation_date.strftime('%a, %d %b %Y %H:%M:%S ') 
        post_text = post.text
        
        xml_rs += u'<posts_item>'               
        xml_rs += u'<author>%s</author>' % post_author 
        xml_rs += u'<link>%s://%s%s</link>' % (protocol, host, reverse('gb_main_page'))
        xml_rs += u'<pub_date>%s+0400</pub_date>' % post_date               
        xml_rs += u'<text>%s</text>' % post_text
        xml_rs += u'</posts_item>'
    xml_rs += u'</posts_list>'
       
    return HttpResponse(xml_rs, content_type="application/xml")
                             
                                 
# страница с перечнем авторов
def list_users(request):
    # paginator
    names_list = GuestBookPost.objects.values_list('name', flat=True).distinct()
    paginator = Paginator(names_list, 5)
    page = request.GET.get('page')
    try:
        names = paginator.page(page)    
    except PageNotAnInteger:
        names = paginator.page(1)    
    except EmptyPage:
        names = paginator.page(paginator.num_pages)
    
    return render_to_response('gbook/list_users.html', {'names':names}, context_instance=RequestContext(request))


# страница с постами какого-то из авторов
def user_posts(request):
    # paginator
    name = request.GET.get('name') 
    name_posts_list = GuestBookPost.objects.filter(name=name).values()
    paginator = Paginator(name_posts_list, 2)
    page = request.GET.get('page')
    try:
        name_posts = paginator.page(page)              
    except PageNotAnInteger:
        name_posts = paginator.page(1)    
    except EmptyPage:
        name_posts = paginator.page(paginator.num_pages)
         
    return render_to_response('gbook/user_posts.html', 
                              {'name':name, 
                               'name_posts':name_posts,
                              }, 
                             context_instance=RequestContext(request))                            
      