from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    register_time = models.DateTimeField(auto_now_add=True)
    head_pic = models.ImageField(upload_to='head_picture')
    user_info = models.CharField(max_length=100, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    salt = models.CharField(max_length=50, blank=True, null=True)