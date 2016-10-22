from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings
import requests


def index(request):
    context = {}
    template = "home.html"
    return render(request, template, context)


def page_not_found(request):
    url = request.get_full_path()
    img = static('img/404.png')
    home = settings.SHARE_URL
    template = "error.html"
    context = {"url": home + url, "error": 404, "error_text": "Page not found.", "img": img, "home": home}
    return render(request, template, context)


def server_error(request):
    url = request.get_full_path()
    home = settings.SHARE_URL
    img = static('img/500.png')
    template = "error.html"
    context = {"url": home + url, "error": 500, "error_text": "Sorry, but the requested page is unavailable due to a server hiccup.", "img": img, "home": home}
    return render(request, template, context)
