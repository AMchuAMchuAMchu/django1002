from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def yukino(request):
    return HttpResponse('雪之下雪乃-冰雪女王,要说她是何等美貌,是让人无法触及更无法得到的,只能让人为之惊叹其美丽的存在...');

def psychopass(request):
    return render(request,'psychopass.html')

def index(request):
    return render(request,'index.html')