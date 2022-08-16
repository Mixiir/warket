from .constants import COUNTRIES, LANGUAGES, WINE_VARIETY, WINE_TYPE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, choices=COUNTRIES, blank=True, null=True)
    language = models.CharField(max_length=100, choices=LANGUAGES, blank=True, null=True)
    seller = models.BooleanField(default=False)
    buyer = models.BooleanField(default=False)
    auctioneer = models.BooleanField(default=False)
    auction_limit = models.PositiveIntegerField(blank=True, null=True)
    sold_items = models.PositiveIntegerField(default=0)
    feedback_score = models.PositiveIntegerField(blank=True, null=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, choices=COUNTRIES)
    region = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Wine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    vintage = models.PositiveIntegerField(blank=True, null=True)
    alcohol_content = models.FloatField(blank=True, null=True)
    price_per_unit = models.PositiveIntegerField(blank=True, null=True)
    units_in_stock = models.PositiveIntegerField(blank=True, null=True)
    units_in_auction = models.PositiveIntegerField(blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True, choices=WINE_TYPE)
    variety = models.CharField(max_length=100, blank=True, null=True, choices=WINE_VARIETY)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    total = models.PositiveIntegerField(blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    date_modified = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.CharField(max_length=100, blank=True, null=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    payment_amount = models.PositiveIntegerField(blank=True, null=True)
    payment_currency = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    payment_details = models.TextField(blank=True, null=True)
