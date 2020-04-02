from django.db import models


# Create your models here.
class books(models.Model):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=45, null=True)
    website = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    publisher = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=45, null=True)
    url = models.CharField(max_length=400, null=True)
    cover = models.CharField(max_length=400, null=True)
