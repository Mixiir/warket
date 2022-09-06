from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id} : {self.name}"


class AuctionListing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    start_bid = models.DecimalField(decimal_places=2, max_digits=7)
    max_bid = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True, default="default.jpg")
    end_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    comments_allowed = models.BooleanField(default=True)
    last_bidder = models.CharField(max_length=50, blank=True, null=True)
    auction_period = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.id}: " \
               f"{self.name}\n " \
               f"{self.category.name}\n" \
               f"Posted at :{self.date}\n " \
               f"Value : {self.start_bid}\n" \
               f"Description : {self.description}\n" \
               f"Posted By : {self.user.username}\n" \
               f"Active Status: {self.active}\n" \
               f"Max bid: {self.max_bid}\n" \
               f"Last bidder: {self.last_bidder}\n" \
               f"Auction period: {self.auction_period}\n" \
               f"Image URL : {self.image_url}\n" \
               f"Comments allowed: {self.comments_allowed}\n" \
               f"End date: {self.end_date}\n"


class Bid(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_value = models.DecimalField(decimal_places=2, max_digits=10)
    auctionListing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)


def __str__(self):
    return f"{self.id} : {self.user.username} bid {self.bid_value} on {self.auctionListing.name} at {self.date}"


class Comment(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionListing = models.ForeignKey(
        AuctionListing, on_delete=models.CASCADE)
    commentValue = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.id} : " \
               f"{self.user.username} commented on " \
               f"{self.auctionListing.name} posted by " \
               f"{self.auctionListing.user.username} at " \
               f"{self.date} : " \
               f"{self.commentValue}"
