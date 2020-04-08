from django.urls import path
from main import views
urlpatterns = [
    path('main/', views.main, name='main'),
    path('login/', views.login_form, name='login'),
    path('get_code/', views.get_code, name='get_code'),
    path('check_user/', views.check_user, name='check_user'),
]
