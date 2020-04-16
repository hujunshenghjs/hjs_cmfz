from django.shortcuts import render

# Create your views here.
import hashlib
import random

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from main.models import *


def first_page(request):
    """
    一级页面接口
    :param request: uid,type,sub_type,GET
    :return:Json
    """
    try:
        user_id = request.GET.get("uid")
        # 首页：all，闻：wen，思：si
        type = request.GET.get("type")
        # 上师言教：ssyj，显密法要：xmfy
        sub_type = request.GET.get("sub_type")
        print(user_id, type, sub_type)

        if not user_id:
            return JsonResponse({"status": 401, 'msg': '用户未登录'})

        album = []
        # 专辑
        album_qset = TAlbum.objects.all()
        for album_model in album_qset:
            album.append({
                "thumbnail": "http://127.0.0.1:8000/static/" + str(album_model.thumbnail_url),
                "title": album_model.album_title,  # 标题
                "author": album_model.author,  # 描述
                "type": "0",  # 类型（0：闻）
                "set_count": album_model.chapter_num,  # 集数（只有闻的数据才有）
                "create_date": album_model.publish_time  # 创建时间
            })
        # 文章

        ssyj = []
        xmfy = []
        article_qset = TArticle.objects.all()
        for article_model in article_qset:
            if article_model.article_category == 1:
                ssyj.append({
                    "thumbnail": "http://127.0.0.1:8000/static/" + str(article_model.thumbnail_url),
                    "title": article_model.title,  # 标题
                    "content": article_model.content,
                    "article_category": article_model.article_category,
                    "type": "1",  # 类型（1：思）
                    "create_date": article_model.publish_date  # 创建时间
                })
            else:
                xmfy.append({
                    "thumbnail": "http://127.0.0.1:8000/static/" + str(article_model.thumbnail_url),
                    "title": article_model.title,  # 标题
                    "content": article_model.content,
                    "article_category": article_model.article_category,
                    "type": "1",  # 类型（1：思）
                    "create_date": article_model.publish_date  # 创建时间
                })
        article = ssyj + xmfy
        # 代表访问的事首页
        if type == "all":
            # 查询首页所需的数据并按规定的格式响应回去
            # 轮播图
            slid_pic_qset = TSlidpic.objects.all()
            slid_pic = []
            for pic_model in slid_pic_qset:
                slid_pic.append({
                    "thumbnail": "http://127.0.0.1:8000/static/" + str(pic_model.url),
                    "desc": pic_model.title,  # 头图描述
                    "id": pic_model.id  # 头图id
                })
            return JsonResponse({
                'status': 1,
                'slid_pic': slid_pic,
                'body': album + article,
            })
        elif type == "wen":
            # 代表范文的是专辑 查询专辑的信息响应回去
            return JsonResponse({
                'status': 1,
                'album': album,
            })
        elif type == "si":
            if sub_type == "ssyj":
                # 查询属于上师言教的文章
                return JsonResponse({
                    'status': 1,
                    'ssyj': ssyj,
                })
            else:
                # 查询属于显密法要的文章
                return JsonResponse({
                    'status': 1,
                    'xmfy': xmfy,
                })
    except BaseException as error:
        return HttpResponse(f'查询错误{error}')
    return HttpResponse(f'first_page参数错误')


def wen(request):
    """
    专辑的详情页接口
    :param request:id专辑id，由上一页面列表传过来,uid
    :return:Json
    """
    try:
        album_id = int(request.GET.get('album_id'))
        album_model = TAlbum.objects.get(id=album_id)
        chapter_qset = TAudioChapter.objects.filter(audio_id=album_model.id)
        introduction = {  # 详情简介
            "thumbnail": "http://127.0.0.1:8000/static/" + str(album_model.thumbnail_url),  # 缩略图
            "title": album_model.album_title,  # 专辑名
            "score": album_model.rating,  # 分数（0 - 5）
            "author": album_model.author,  # 作者
            "broadcast": album_model.bordcaster,  # 播音
            "set_count": album_model.chapter_num,  # 集数
            "brief": album_model.description,  # 内容简介
            "create_date": album_model.publish_time  # 发布日期
        }

        chapter_list = []
        for chapter_model in chapter_qset:
            chapter_list.append({
                "title": chapter_model.chapter_name,  # 第几集
                "download_url": "http://127.0.0.1:8000/static/" + str(chapter_model.audio_url),  # 下载地址
                "size": chapter_model.audio_size + 'k',  # 音频大小（字节数）
                "duration": chapter_model.audio_duration + 's'  # 音频时长（毫秒数）
            })
        return JsonResponse({
            'status': 1,
            'introduction': introduction,
            'list': chapter_list
        })
    except BaseException as error:
        return HttpResponse(f'查询错误{error}')


@csrf_exempt
def register(request):
    """
    注册接口
    :param request:phone,password
    :return:id,加密后密码,手机号
    """
    try:
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        print(phone, password)
        user = TUser.objects.filter(phone=phone)
        if user:
            return JsonResponse({
                "error": "-200",
                "error_msg": "该手机号已经存在"
            })
        else:
            salt = str(random.randint(1000, 9999))
            sha = hashlib.sha1()
            sha.update((password + salt).encode())
            password = sha.hexdigest()
            print(password)
            return JsonResponse({
                "password": password,
                "uid": salt,
                "phone ": phone,
            })
    except BaseException as error:
        return HttpResponse(f'添加账户失败{error}')


@csrf_exempt
def modify(request):
    """
    修改个人信息接口
    :param request:phone,password
    :return:id,加密后密码,手机号
    """
    try:
        uid = request.POST.get('uid')
        gender = request.POST.get('gender')
        photo = request.FILES.get('photo')
        location = request.POST.get('location')
        description = request.POST.get('description')
        nickname = request.POST.get('nickname')
        province = request.POST.get('province')
        city = request.POST.get('city')
        password = request.POST.get('password')
        try:
            user = TUser.objects.get(user_id=uid)
            salt = str(random.randint(1000, 9999))
            sha = hashlib.sha1()
            sha.update((password + salt).encode())
            password = sha.hexdigest()
            print(password)
            return JsonResponse({
                "password": password,  # MD5后的密码
                "farmington": nickname,  # 法名
                "uid": salt,  # 用户id
                "nickname": nickname,  # 昵称
                "gender": gender,  # 性别（m：男 f：女）
                "photo": "userthumbnail/" + str(photo),  # 头像
                "location": location,  # 所在地
                "province": province,  # 省市
                "city": city,  # 地区
                "description": description,  # 个人签名
                "phone ": user.phone  # 手机号
            })

        except BaseException as error:
            return JsonResponse({
                "error": "-200",
                "error_msg": f"该用户不存在{error}"
            })
    except BaseException as error:
        return HttpResponse(f'添加账户失败{error}')