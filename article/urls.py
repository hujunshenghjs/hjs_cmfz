from django.urls import path
from article import views

urlpatterns = [
    path('load_kind/', views.load_kind, name='load_kind'),
    path('upload/', views.upload_img, name='upload_img'),
    path("get_all_img/", views.get_all_img),
    path("add_article/", views.add_article),
]
