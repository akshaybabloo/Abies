from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import requests


def index(request):
    return HttpResponse("Coming soon")