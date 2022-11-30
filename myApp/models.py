from django.db import models

# Create your models here.
class Feature(models.Model):
    title = models.CharField(default="title1",max_length=100)
    description = models.CharField(default="description to the title1", max_length=500)
    extendable = models.BooleanField


class Blog(models.Model):
    title = models.CharField(default="title1",max_length=100)
    description = models.CharField(default="description to the title1", max_length=500)
