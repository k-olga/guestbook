#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from django import forms


class GuestBookForm(forms.Form):
    name = forms.CharField(max_length=15, label=u'Имя', 
                           error_messages={'required': u'Пожалуйста, введите Ваше имя'})
    text = forms.CharField(max_length=300, label=u'Сообщение', 
                           error_messages={'required': u'Пожалуйста, введите Ваше сообщение'}, widget=forms.Textarea)
    error_css_class = 'error'
    required_css_class = 'required'
        
    def clean(self):
        cleaned_data = super(GuestBookForm, self).clean()
        name = cleaned_data.get('name')
        regexp = re.compile(r'^[^0-9]\w+$')                        
                   
        if name:
            false_name = u'Проверьте правильность написания имени!'
            if regexp.search(name) == None:
                self._errors["name"] = self.error_class([false_name])
                del cleaned_data["name"]
            
        return self.cleaned_data  
          
         