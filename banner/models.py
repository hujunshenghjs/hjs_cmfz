from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
class Banner(models.Model):
    picture_title = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_created=True, auto_now_add=True)
    picture_status = models.BooleanField()
    picture_url = models.ImageField(max_length=100, null=True, upload_to="pictures")
