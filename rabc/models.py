from django.db import models

# Create your models here.
from django.db import models
from django.db.models import DO_NOTHING


class Permission(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)
    is_menu = models.BooleanField(verbose_name="是否是菜单", default=False)
    sup_menu_id = models.ForeignKey(verbose_name='父菜单id', to='SupMenu', blank=True, on_delete=DO_NOTHING, null=True)

    def __str__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)
    roles = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)

    def __str__(self):
        return self.name


class SupMenu(models.Model):
    name = models.CharField(verbose_name='父菜单名称', max_length=64)

    def __str__(self):
        return self.name