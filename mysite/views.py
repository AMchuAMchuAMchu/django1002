import datetime

from django.shortcuts import render

# Create your views here.

def index(request):
    print(datetime.datetime.now(),'::有人访问了index...')
    return render(request,'index.html')

def login(request):
    print(datetime.datetime.now(),'::有人访问了login...')
    return render(request,'login.html')

user_list = [
    {'username':'雪之下雪乃','password':'5201314'},
    {'username':'堀北铃','password':'5202020'},
]

def success_login(request):
    if request.method == 'POST':
        print(datetime.datetime.now(),'::有人访问了success_login...')
        print('用户名:',request.POST.get('username'))
        print('密 码:',request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = {'username':username,'password':password}
        user_list.append(user)
        return render(request,'success_login.html',{'data':user_list})



