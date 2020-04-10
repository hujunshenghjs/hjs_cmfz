from django.urls import path

from user import views

urlpatterns = [
    path("user_distribution/", views.user_distribution, name="user_distribution"),
    path("user_register_trend/", views.user_register_trend, name="user_register_trend"),
]