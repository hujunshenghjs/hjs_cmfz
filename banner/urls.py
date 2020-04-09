from django.urls import path

from banner import views
app_name = "banner"
urlpatterns = [
    path("get_all_banner/", views.get_all_banner, name="get_all_banner"),
    path("add_banner/", views.add_banner, name="add_banner"),
]