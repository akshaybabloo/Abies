"""Abies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('viewer.urls')),
    url(r'^editor/', include('editor.urls'), name='editor_urls'),
    url(r'^welcome/', include('welcome.urls'), name='welcome_urls'),
    url(r'^settings/', include('settings.urls')),
    url(r'^admin/', admin.site.urls, name='admin_urls'),
]

handler404 = 'viewer.views.page_not_found'
handler500 = 'viewer.views.server_error'
