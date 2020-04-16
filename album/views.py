from django.shortcuts import render

# Create your views here.
import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from main.models import *
from django.views.decorators.csrf import csrf_exempt


def getAllAlbum(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    album = TAlbum.objects.all().order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)

    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, TAlbum):
            return {
                "author": u.author,
                "brief": u.description,
                "broadcast": u.bordcaster,
                "count": u.chapter_num,
                "cover": u.thumbnail_url,
                "createDate": u.publish_time.strftime('%Y-%m-%d %H:%M:%S'),
                "id": u.id,
                "publishDate": u.publish_time.strftime('%Y-%m-%d %H:%M:%S'),
                "score": '%.1f' % u.rating,
                "status": u.status,
                "title": u.album_title,
            }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


@csrf_exempt
def editAlbum(request):
    method = request.POST.get('oper')
    print(method)
    author = request.POST.get("author")
    brief = request.POST.get("brief")
    broadcast = request.POST.get("broadcast")
    count = request.POST.get("count")
    cover = request.FILES.get("cover")
    create_date = request.POST.get("createDate")
    id = request.POST.get("id")
    publish_date = request.POST.get("publishDate")
    score = request.POST.get("score")
    status = request.POST.get("status")
    title = request.POST.get("title")
    print(f'id: {id} 作者：{author}简介：{brief}播音员:{broadcast}章节数量:{count} 封面：{cover} 创建日期{create_date} 发布日期{publish_date}'
          f'评分:{score} 状态：{status} 标题：{title}')
    if method == 'add':
        try:
            # TAlbum.objects.create(album_title=title, author=author, bordcaster=broadcast, chapter_num=count,
            #                       description=brief, rating=score, status=status)
            return JsonResponse({'status': 1, 'msg': f'添加成功！'})
        except BaseException as error:
            return JsonResponse({'status': 0, 'msg': f'添加失败！{error}'})
    elif method == 'edit':
        try:
            album = TAlbum.objects.get(id=id)
            album.album_title = title
            album.rating = score
            album.bordcaster = broadcast
            album.description = brief
            album.status = status
            album.save()
            return JsonResponse({'status': 1, 'msg': f'修改成功！'})
        except BaseException as error:
            return JsonResponse({'status': 0, 'msg': f'添加失败！{error}'})
    elif method == 'del':
        try:
            album = TAlbum.objects.get(id=id)
            album.delete()
            return JsonResponse({'status': 1, 'msg': f'删除成功！'})
        except BaseException as error:
            return JsonResponse({'status': 0, 'msg': f'添加失败！{error}'})
    return HttpResponse()


def getChapterByAlbumId(request):
    album_Id = request.GET.get('albumId')
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')
    print(album_Id, page_num, row_num)

    rows = []
    album = TAudioChapter.objects.all().filter(audio_id=album_Id).order_by('id')
    all_page = Paginator(album, row_num)
    page = all_page.page(page_num)

    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, TAudioChapter):
            return {
                "albumId": u.audio_id,
                "createDate": u.publish_time.strftime('%Y-%m-%d %H:%M:%S'),
                "duration": u.audio_duration,
                "id": u.id,
                "size": u.audio_size,
                "title": u.chapter_name,
                "url": str(u.audio_url),
            }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


@csrf_exempt
def add_chapter(request):
    title = request.POST.get('title')
    status = request.POST.get('status')
    audio = request.FILES.get('audio')
    albumId = request.POST.get("albumId")
    # 音频大小
    size = audio.size

    # 音频时长
    audio_mp3 = MP3(audio)
    duration = audio_mp3.info.length
    duration = '%.1f' % duration
    print(title, status, audio, duration, size, f'albumid:{albumId}', )
    try:
        TAudioChapter.objects.create(chapter_name=title,
                                     audio_url=audio,
                                     audio_size=size,
                                     audio_duration=duration,
                                     audio_id=albumId)
        print(111)
    except BaseException as error:
        print(error)

    return HttpResponse()


@csrf_exempt
def editChapter(request):
    method = request.POST.get('oper')
    if method == 'del':
        id = request.POST.get('id')
        try:
            chapter = TAudioChapter.objects.get(id=id)
            chapter.delete()
        except BaseException as error:
            print(error)
    return HttpResponse()
