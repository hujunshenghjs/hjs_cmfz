import json, os, uuid, time

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from user.models import User
import datetime


def user_register_trend(request):
    from redis import Redis
    redis = Redis(host='192.168.0.103', port=6379)
    if redis.get("data"):
        data = eval(redis.get("data"))
    else:
        now = time.strftime("%Y-%m-%d")
        day1 = (datetime.date.today() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")
        day2 = (datetime.date.today() + datetime.timedelta(days=-6)).strftime("%Y-%m-%d")
        day3 = (datetime.date.today() + datetime.timedelta(days=-5)).strftime("%Y-%m-%d")
        day4 = (datetime.date.today() + datetime.timedelta(days=-4)).strftime("%Y-%m-%d")
        day5 = (datetime.date.today() + datetime.timedelta(days=-3)).strftime("%Y-%m-%d")
        day6 = (datetime.date.today() + datetime.timedelta(days=-2)).strftime("%Y-%m-%d")
        day7 = (datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        x = [now, day7, day6, day5, day4, day3, day2, day1]
        y = []
        for i in range(7):
            num = len(list(User.objects.filter(register_time__gt=x[i + 1], register_time__lt=x[i])))
            y.append(num)
        x = [day7, day6, day5, day4, day3, day2, day1]
        data = {
            'x': x,
            'y': y,
        }
        print(data)
        redis.set("data", str(data), 24 * 60 * 60)
    print(data)
    return JsonResponse(data)


def user_distribution(request):
    data = [
        {'name': '北京', 'value': 0},
        {'name': '天津', 'value': 0},
        {'name': '广东', 'value': 0},
        {'name': '上海', 'value': 0},
        {'name': '重庆', 'value': 0},
        {'name': '河北', 'value': 0},
        {'name': '河南', 'value': 0},
        {'name': '云南', 'value': 0},
        {'name': '辽宁', 'value': 0},
        {'name': '湖南', 'value': 0},
        {'name': '安徽', 'value': 0},
        {'name': '⼭东', 'value': 0},
        {'name': '新疆', 'value': 0},
        {'name': '江苏', 'value': 0},
        {'name': '浙江', 'value': 0},
        {'name': '江⻄', 'value': 0},
        {'name': '湖北', 'value': 0},
        {'name': '⼴⻄', 'value': 0},
        {'name': '⽢肃', 'value': 0},
        {'name': '⼭⻄', 'value': 0},
        {'name': '陕⻄', 'value': 0},
        {'name': '吉林', 'value': 0},
        {'name': '福建', 'value': 0},
        {'name': '贵州', 'value': 0},
        {'name': '⻘海', 'value': 0},
        {'name': '⻄藏', 'value': 0},
        {'name': '四川', 'value': 0},
        {'name': '宁夏', 'value': 0},
        {'name': '海南', 'value': 0},
        {'name': '台湾', 'value': 0},
        {'name': '⾹港', 'value': 0},
        {'name': '澳⻔', 'value': 0}
    ]
    for i in data:
        users = User.objects.filter(address=i['name'])
        i['value'] = len(users)
    return JsonResponse(data, safe=False)