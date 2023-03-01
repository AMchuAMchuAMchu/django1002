import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    print(datetime.datetime,'::有人访问了index...')
    return render(request,'index.html')

def login(request):
    print(datetime.datetime,'::有人访问了login...')
    return render(request,'success.html')

