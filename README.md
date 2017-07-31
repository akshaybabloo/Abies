> Caution: This repo is not maintained anymore. See [gollahalli-com](https://github.com/akshaybabloo/gollahalli-com) for a different implementation.

# Abies

:evergreen_tree: A Django based all-in-one web creator.

> Under development

**Table of Contents**

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [1 About the application](#1-about-the-application)
- [2 Additional files needed](#2-additional-files-needed)
	- [2.1 About `__init__.py`](#21-about-initpy)
	- [2.2 About `base.py`](#22-about-basepy)
	- [2.3 About `local.py`](#23-about-localpy)
	- [2.4 About `common.py`](#24-about-commonpy)
	- [2.5 About `secrets.py`](#25-about-secretspy)
		- [2.5.1 Generating keys in Django style](#251-generating-keys-in-django-style)
- [3 What next?](#3-what-next)

<!-- /TOC -->

## 1 About the application

`viewer` is the font-end and `editor` is the back-end.

## 2 Additional files needed

The structure of this app is in such a way that it could be used to run on Heroku or on your local machine.

The main focus should be on `/settings/` under 'Abies' folder, this folder contains the following files

<pre>

settings
|
+-- __init__.py
+-- base.py
+-- local.py (ignored)
+-- common.py
+-- secrets.py (ignored)
'-- production.py

</pre>

### 2.1 About `__init__.py`

This file is self-explanatory, if `local.py` is not found `production.py` is loaded.

### 2.2 About `base.py`

This file acts as a base to the application; this file is loaded when the application starts.

### 2.3 About `local.py`

> This file is optional, but you will need it if you are planning it to run on your local machine.

This file contains almost everything in `base.py`, but it is only for your local system. The following is its content, just copy the code, create a file called `local.py` under `/settings/` folder and paste it.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

"""
Django settings for Abies project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from .secrets import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = In secrets.py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Abies.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Abies.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# Common stuff
from .common import *
```

### 2.4 About `common.py`

This file contains all the common stuff that needs to be used in `local.py` and `base.py`.

### 2.5 About `secrets.py`

Before you start the Django app, you would have to create `secrets.py` file under `Abies -> settings -> secrets.py`. This file consists of the following

```python
SECRET_KEY = '{{ Your Secret Key }}'# Enter your 50 character secret key
```
Use [1.5.1](#151-generating-keys-in-django-style) to generate the key.

#### 2.5.1 Generating keys in Django style

Using Django's crypto package, you can generate random `50` character long key.

```python
from __future__ import print_function
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = get_random_string(50, chars)

print(SECRET_KEY)

```

## 3 What next?

Once you have all the files in the place, do the following:

Open Terminal (Linux) or Command Prompt (Windows), navigate to `Abies` folder and type in the following, which will create your database file and create an admin user:

```python
python manage.py migrate
python manage.py createsuperuser
```

## 4 Running `run.ps1`

To run the PowerShell script, do the following:

```
powershell -ExecutionPolicy ByPass -File run.ps1
```

## 5 Running `run.sh`

To run the Bash script, do the following:

```
sh run.sh
```
