from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from rabc.models import *
from rabc.service.init_permission import init_permission


def login(request):
    return render(request, 'login_form.html')


def check_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    try:
        user = UserInfo.objects.get(name=username, password=password)
        # 处理权限相关的业务
        init_permission(user, request)

        return JsonResponse({'status': 1})

    except BaseException as error:
        return JsonResponse({'status': 0, 'msg': f'用户名或密码错误{error}'})