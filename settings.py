#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, '/home/tim/djprojects/guestbook')
sys.path.insert(0, '/home/tim/djprojects/guestbook/apps')

BASE_DIR = os.path.normpath('/home/tim/djprojects/guestbook/')

SECRET_KEY = 'x&i2il&29k5msjutbhzjjhkoiuoi%%ym9x9^dtrtt'

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (
    ('Kozub Olga', 'os.kozub@yandex.ru'),
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',     # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'guestbook',                      # Or path to database file if using sqlite3.
        'USER': 'user',                           # Not used with sqlite3.
        'PASSWORD': 'Diuyi456',                   # Not used with sqlite3.
        'HOST': '',                               # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                               # Set to empty string for default. Not used with sqlite3.
    }
}

DEFAULT_CHARSET = 'utf-8'

SITE_ID = 1 

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (   
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.csrf',
    'django.core.context_processors.request', 
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'templates/gbook/locale'),
)

USE_I18N = True
USE_L10N = True

TIME_ZONE = 'Europe/Moscow'
USE_TZ = True
LANGUAGE_CODE = 'en-us'

ROOT_URLCONF = 'urls'


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.messages',
    'django.contrib.syndication',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'gbook',
)





WSGI_APPLICATION = 'wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/



    