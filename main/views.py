from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from redis import Redis
from hjs_cmfz import settings
from utils.send_mess import yunpian
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from utils import random_number
from utils import send_mess
import re


def main(request):
    return render(request, "main.html")


def login_form(request):
    return render(request, "login.html")


redis = Redis(host='localhost', port=6379)
@csrf_exempt
def get_code(request):
    mobile = request.POST.get("mobile")
    print(mobile)
    if mobile:
        value = redis.get(f'{mobile}_1')
        print(value)
        if value:
            return JsonResponse({'status': 0, 'msg': '验证码已发送'})
        code = send_mess.d
        print(code)
        yun = yunpian(settings.APIKEY)
        # yun.send_message(mobile, code)
        redis.set(f"{mobile}_1", code, 1)
        redis.set(f"{mobile}_2", code, 1)
        return JsonResponse({'status': 1, 'msg': '发送成功!'})
    else:
        return JsonResponse({'status': 0, 'msg': '请输入合法的手机号！'})


def check_user(request):
    mobile = request.GET.get("mobile")
    name = request.GET.get("name")
    code = request.GET.get("code")
    print(mobile, name, code, "111111111")
    mobile_check = re.match(r"^1[35678]\d{9}$", mobile)
    code_check = re.match(r"\d{6}$", code)
    if mobile_check and code_check:
        try:
            save_code = redis.get(f'{mobile}_2')
            print(save_code, "2231313")
            if save_code.decode() == code:
                print("111")
                return JsonResponse({'status': 1, 'msg': '登陆成功！'})
        except BaseException as error:
            print(error)
            return JsonResponse({'status': 0, 'msg': f'{error}请发送验证码！'})
        return JsonResponse({'status': 0, 'msg': '登陆失败！'})
    else:
        return JsonResponse({'status': 0, 'msg': '输入不合法'})
