from django.db import models


class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length = 10)
# Create your models here.
