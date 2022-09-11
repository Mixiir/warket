from django.contrib import admin

from .models import AuctionListing, Bid, Category, Comment

admin.site.register(Category)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)
