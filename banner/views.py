from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import os, uuid, json
from banner.models import Banner


def get_all_banner(request):
    banner_list = Banner.objects.all().order_by('id')
    rows = request.GET.get('rows')
    page = request.GET.get('page', 1)
    pagtor = Paginator(banner_list, per_page=rows)  # 分页器对象
    q = list(pagtor.page_range)
    if int(page) not in q:
        page = 1
    all_page = Paginator(banner_list, rows)
    # 获取分页后第一页的对象
    page_obj = Paginator(banner_list, rows).page(page).object_list
    page_data = {
        "page": page,
        "total": all_page.num_pages,
        "records": all_page.count,
        "rows": list(page_obj)
    }

    # 对象序列化
    def myDefault(b):
        if isinstance(b, Banner):
            return {"id": b.pk,
                    "desc": b.picture_title,
                    "status": '展示' if b.picture_status == 1 else '不展示',
                    "pic": str(b.picture_url),
                    "date": b.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                    }

    data = json.dumps(page_data, default=myDefault)
    print(data)
    return HttpResponse(data)


@csrf_exempt
def add_banner(request):
    title = request.POST.get("title")
    status = request.POST.get('status')
    picture = request.FILES.get('pic')
    print(title, status, picture, "111111")
    try:
        result = Banner.objects.create(picture_title=title, picture_status=str(status), picture_url=picture)
        if result:
            return HttpResponse('添加成功！')
    except BaseException as error :
        print(error)
        return HttpResponse('添加失败！')


@csrf_exempt
def edit_banner(request):
    method = request.POST.get("oper")
    if method == 'edit':
        id = request.POST.get('id')
        title = request.POST.get('desc')
        status = request.POST.get('status')
        print(id,status,title)
        pic = Banner.objects.get(pk=id)
        pic.picture_title= title
        pic.picture_status = status
        pic.save()
        return HttpResponse('修改成功')

    elif method == 'del':
        id = request.POST.get('id')
        pic = Banner.objects.get(pk=id)
        pic.delete()
        return HttpResponse('删除成功')