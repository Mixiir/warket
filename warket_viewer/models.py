import base64
from io import BytesIO

import PIL.Image
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from PIL import Image

from .constants import COUNTRIES, WINE_TYPE


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="default.jpg", upload_to="images")
    country = models.CharField(max_length=100, choices=COUNTRIES)
    region = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Wine(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="default.jpg", upload_to="images")
    thumbnail = models.ImageField(default="default.jpg", upload_to="images")
    description = models.TextField()
    rating = models.FloatField(default=0)
    vintage = models.PositiveIntegerField(default=1999)
    alcohol_content = models.FloatField(blank=True, null=True)
    price_per_unit = models.PositiveIntegerField(default=1)
    units_in_stock = models.PositiveIntegerField(default=1)
    units_in_auction = models.PositiveIntegerField(default=0)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=100, choices=WINE_TYPE, default="red")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)





