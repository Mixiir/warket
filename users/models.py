import django.utils.timezone
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from warket_viewer.constants import COUNTRIES


class MyUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    birth_date = models.DateField(default="1999-01-01")
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        _("date joined"),
        default=django.utils.timezone.now
    )
    image = models.ImageField(
        default="default.jpg",
        upload_to="profile_pics"
    )
    country = models.CharField(
        max_length=50,
        choices=COUNTRIES,
        default="United States"
    )
    bio = models.TextField(
        max_length=500,
        blank=True
    )
    language = models.CharField(
        max_length=50,
        choices=COUNTRIES,
        default="English"
    )
    seller = models.BooleanField(default=False)
    buyer = models.BooleanField(default=False)
    auctioneer = models.BooleanField(default=False)
    auction_limit = models.PositiveIntegerField(default=0)
    sold_wines = models.PositiveIntegerField(default=0)
    bought_wines = models.PositiveIntegerField(default=0)
    auctioned_wines_bought = models.PositiveIntegerField(default=0)
    auctioned_wines_sold = models.PositiveIntegerField(default=0)
    objects = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "birth_date"]
