from django.urls import path

from banner import views

urlpatterns = [
    path("get_all_banner/", views.get_all_banner),
    path("add_banner/", views.add_banner),
]