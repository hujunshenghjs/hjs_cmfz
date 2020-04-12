import json, os, uuid, time

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from user.models import User
import datetime


# def user_register_trend(request):
#     from redis import Redis
#     redis = Redis(host='192.168.0.103', port=6379)
#     if redis.get("data"):
#         data = eval(redis.get("data"))
#     else:
#         now = time.strftime("%Y-%m-%d")
#         day1 = (datetime.date.today() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")
#         day2 = (datetime.date.today() + datetime.timedelta(days=-6)).strftime("%Y-%m-%d")
#         day3 = (datetime.date.today() + datetime.timedelta(days=-5)).strftime("%Y-%m-%d")
#         day4 = (datetime.date.today() + datetime.timedelta(days=-4)).strftime("%Y-%m-%d")
#         day5 = (datetime.date.today() + datetime.timedelta(days=-3)).strftime("%Y-%m-%d")
#         day6 = (datetime.date.today() + datetime.timedelta(days=-2)).strftime("%Y-%m-%d")
#         day7 = (datetime.date.today() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
#         x = [now, day7, day6, day5, day4, day3, day2, day1]
#         y = []
#         for i in range(7):
#             num = len(list(User.objects.filter(register_time__gt=x[i + 1], register_time__lt=x[i])))
#             y.append(num)
#         x = [day7, day6, day5, day4, day3, day2, day1]
#         data = {
#             'x': x,
#             'y': y,
#         }
#         print(data)
#         redis.set("data", str(data), 24 * 60 * 60)
#     print(data)
#     return JsonResponse(data)

def load_register(request):
    return render(request, "echarts.html")


def get_register(request):
    x = ["1", "2", "3", "4", "5", "6", "7"]
    y = [100, 20, 12, 53, 48, 12, 45]
    data = {
        'x': x,
        'y': y
    }
    return JsonResponse(data)


def load_map(request):
    return render(request, 'map.html')

def get_map(request):
    data = [
        {"name": '北京', "value": 134},
        {"name": '天津', "value": 245},
        {"name": '上海', "value": 332},
        {"name": '重庆', "value": 422},
        {"name": '河北', "value": 534},
        {"name": '河南', "value": 656},
        {"name": '云南', "value": 723},
        {"name": '辽宁', "value": 834},
        {"name": '湖南', "value": 923},
        {"name": '安徽', "value": 924},
        {"name": '山东', "value": 823},
        {"name": '新疆', "value": 734},
        {"name": '江苏', "value": 632},
        {"name": '浙江', "value": 554},
        {"name": '江西', "value": 423},
        {"name": '湖北', "value": 332},
        {"name": '广西', "value": 222},
        {"name": '甘肃', "value": 112},
        {"name": '山西', "value": 33},
        {"name": '陕西', "value": 23},
        {"name": '吉林', "value": 34},
        {"name": '福建', "value": 54},
        {"name": '贵州', "value": 23},
        {"name": '广东', "value": 45},
        {"name": '青海', "value": 23},
        {"name": '西藏', "value": 35},
        {"name": '四川', "value": 45},
        {"name": '宁夏', "value": 32},
        {"name": '海南', "value": 43},
        {"name": '台湾', "value": 54},
        {"name": '香港', "value": 42},
    ]

    return JsonResponse(data, safe=False)
