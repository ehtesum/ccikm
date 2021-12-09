from django.db import models


# Create your models here.

class Tools(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)
    tool_url = models.CharField(max_length=2083)
    description = models.CharField(max_length=500)
    