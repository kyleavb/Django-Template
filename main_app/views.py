from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('GET index')
    return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')