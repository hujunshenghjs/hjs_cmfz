from django.urls import path, include
from album import views
app_name = 'album'
urlpatterns = [
    path("getAllAlbum/", views.getAllAlbum),
    path("editAlbum/", views.editAlbum),
    path("getChapterByAlbumId/", views.getChapterByAlbumId),
    path("add_chapter/", views.add_chapter),
    path("editChapter/", views.editChapter),
]