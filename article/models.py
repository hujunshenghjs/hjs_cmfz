from django.db import models

# Create your models here.


class Article(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    guru_id = models.CharField(max_length=11, blank=True, null=True)
    new_img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class Pic(models.Model):
    img = models.ImageField(upload_to='img')

    class Meta:
        db_table = 't_pic'