import json
import os

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt

from article.models import Article, Pic


def load_kind(request):
    return render(request, "kindeditor.html")


@xframe_options_sameorigin  # 允许页面嵌套时发起访问
@csrf_exempt
def upload_img(request):
    """
    富文本上传图片所使用的的方法
    :param request: 文件
    :return:{"error":0,"url":"\/ke4\/attached\/W020091124524510014093.jpg"}
    图片所在的服务器路径
    """

    file = request.FILES.get("imgFile")

    if file:
        # 获取图片所在的服务的全路径
        img_url = request.scheme + "://" + request.get_host() + "/static/img/" + str(file)
        print("图片路径是：" + img_url)
        result = {"error": 0, "url": img_url}
        Pic.objects.create(img=file)
    else:
        result = {"error": 1, "url": "上传失败"}
    return HttpResponse(json.dumps(result), content_type="application/json")



def get_all_img(request):
    """
    获取所有图片的方法
    :param request:
    :return:
    """
    # 找到图片所在的目录  方便进行回显
    pic_dir = request.scheme + "://" + request.get_host() + '/static/'
    print(pic_dir, "11111111111111")
    pic_list = Pic.objects.all()

    rows = []

    for i in list(pic_list):
        # 获取图片的后缀
        path, pic_suffix = os.path.splitext(i.img.url)
        rows.append({
            "is_dir": False,
            "has_file": False,
            "filesize": i.img.size,
            "dir_path": "",
            "is_photo": True,
            "filetype": pic_suffix,
            "filename": i.img.name,
            "datetime": "2018-06-06 00:36:39"
        })

    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": pic_dir,
        "total_count": len(pic_list),
        "file_list": rows

    }

    return HttpResponse(json.dumps(data), content_type="application/json")


def add_article(request):
    """
    添加文章的方法
    :param request:
    :return:
    """

    category = request.GET.get('category')
    title = request.GET.get('title')
    content = request.GET.get('content')
    print(category, title, content)

    # 可以根据获取到的值进行保存

    return HttpResponse()
