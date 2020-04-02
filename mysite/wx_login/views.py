from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#def wx_login(request):
#    return HttpResponse("Hello, world. You're at the wx test index.")

from .models import User

from django.http import HttpResponse

def wx_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        try:
            user = User.objects.get(userAccount=username)
            if user.userPasswd != passwd:
                return HttpResponse('用户名或密码错误')
        except User.DoesNotExist as e:
            return HttpResponse("用户名不存在")
        # 登录成功
        print(username)
        print(passwd)
        return HttpResponse("登录成功！")
    else:
        return HttpResponse("请求错误")

def wx_regist(request):
    if request.method == 'POST':
        user = User()
        user.userAccount = request.POST.get('name')
        user.userPasswd = request.POST.get('pwd')
        print(user.userAccount)
        print(user.userPasswd)
        user.save()
        return HttpResponse('注册成功！')