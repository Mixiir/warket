from .models import Category, AuctionListing, Comment, Bid
from django.contrib import admin

admin.site.register(Category)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)
