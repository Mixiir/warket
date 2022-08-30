from django.contrib import admin
from django.contrib import admin
from .models import Category, AuctionListing, Comment, Bid

# Register your models here.


admin.site.register(Category)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)