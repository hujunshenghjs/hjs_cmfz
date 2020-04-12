from django.urls import path

from user import views

urlpatterns = [
    path("get_register/", views.get_register, name="get_register"),
    path("load/", views.load_register, name="load_register"),
    path("load_map/", views.load_map, name="load_map"),
    path("get_map/", views.get_map, name="get_map"),
    # path("user_register_trend/", views.user_register_trend, name="user_register_trend"),
]