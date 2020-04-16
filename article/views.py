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
    print(pic_dir, "123")
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
    status = request.GET.get('status')
    file = request.FILES.get("imgFile")
    print(category, title, content, status)

    # 可以根据获取到的值进行保存
    Article.objects.create(title=title, content=content, status=status, create_date="2019-07-17", publish_date="2019-07-17", new_img=file)

    return JsonResponse({'status': 1, 'msg': f'添加成功！'})

def get_all_article(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    article = Article.objects.all().order_by('id')
    all_page = Paginator(article, row_num)
    page = Paginator(article, row_num).page(page_num).object_list

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    for i in page:
        rows.append(i)

    def myDefault(u):
        if isinstance(u, Article):
            return {'id': u.id,
                    'content': u.content,
                    'title': u.title,
                    'category': u.guru_id,
                    'status': u.status == 1,
                    'publish_date': u.publish_date.strftime('%Y-%m-%d %H:%M:%S'),
                    }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)

@csrf_exempt
def edit_article(request):
    method = request.POST.get("oper")
    print(method)
    if method == 'del':
        id = request.POST.get('id')
        Article.objects.get(id=id).delete()
        return JsonResponse({'status': 1, 'msg': f'删除成功！'})
    else:
        id = request.POST.get('id')
        category = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status')
        print(content, id, category, title, status)
        try:
            article = Article.objects.get(id=id)
            article.article_category = category
            article.title = title
            article.content = content
            article.status = status
            article.save()
            return JsonResponse({'status': 1, 'msg': f'修改成功！'})
        except BaseException as error:
            return JsonResponse({'status': 0, 'msg': f'添加失败:{error}'})