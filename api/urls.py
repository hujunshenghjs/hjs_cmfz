from django.urls import path, include
from api import views

app_name = 'api'
urlpatterns = [
    path("first_page/", views.first_page, name='first_page'),
    path("wen/", views.wen, name='wen'),
    path("register/", views.register, name='register'),
    path("modify/", views.modify),
]