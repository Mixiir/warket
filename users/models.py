import django.contrib.auth.validators
import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from warket_viewer.constants import COUNTRIES
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, choices=COUNTRIES, blank=True, null=True)
    language = models.CharField(max_length=100, choices=COUNTRIES, blank=True, null=True)
    seller = models.BooleanField(default=False)
    buyer = models.BooleanField(default=False)
    auctioneer = models.BooleanField(default=False)
    auction_limit = models.PositiveIntegerField(default=0)
    sold_items = models.PositiveIntegerField(default=0)
    feedback_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} Profile"
