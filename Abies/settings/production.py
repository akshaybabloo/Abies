#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

import os

import dj_database_url
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

TEMPLATE_DEBUG = False

DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

SHARE_URL = "http://abies.gollahalli.me/"

# ----------------------------------  S3 Support -------------------------------------
# AWS_ACCESS_KEY_ID = '{{ AWS ID }}'
# AWS_SECRET_ACCESS_KEY = '{{ AWS SECRET KEY }}'
# AWS_STORAGE_BUCKET_NAME = '{{ BUCKET NAME }}'
# AWS_HEADERS = {
#     'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
#     'Cache-Control': 'max-age=86400',
# }
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_CUSTOM_DOMAIN = '{{ CDN URL (optional) }}'
#
# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'custom_storage.StaticStorage'
# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
#
# MEDIAFILES_LOCATION = 'media'
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
# DEFAULT_FILE_STORAGE = 'custom_storage.MediaStorage'
# ---------------------------------------------------------------------------------------

# Comment all the codes below if you are using S3
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'