from django.urls import path
from main import views

urlpatterns = [
    path('main/', views.main),
    path('login/', views.login_form),
    path('get_code/', views.get_code),
]
