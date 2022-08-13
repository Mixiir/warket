from .constants import COUNTRIES, LANGUAGES
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField()
    location = models.CharField(max_length=100, choices=COUNTRIES, blank=True, null=True)
    language = models.CharField(max_length=100, choices=LANGUAGES, blank=True, null=True)
    seller = models.BooleanField(default=False)
    buyer = models.BooleanField(default=False)
    auctioneer = models.BooleanField(default=False)
    auction_limit = models.PositiveIntegerField(blank=True, null=True)
    sold_items = models.PositiveIntegerField(blank=True, null=True)
    feedback_score = models.PositiveIntegerField(blank=True, null=True)


class Wine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, choices=COUNTRIES, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    grape_variety = models.CharField(max_length=100, blank=True, null=True)
    vintage = models.PositiveIntegerField(blank=True, null=True)
    alcohol_content = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)


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
