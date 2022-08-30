from .models import Category, AuctionListing, Bid, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone


def index(request):
    obj = AuctionListing.objects.filter(active=True)
    return render(request, "auctions/index.html", {
        "objects": obj
    })


def all(request):
    obj = AuctionListing.objects.all()
    return render(request, "auctions/index.html", {
        "objects": obj
    })


@login_required
def create_listing(request):
    if request.method == 'POST':
        title = request.POST["title"]
        description = request.POST["description"]
        start_bid = request.POST["start_bid"]
        category = Category.objects.get(id=request.POST["category"])
        user = request.user
        image_url = request.POST["url"]
        if image_url == '':
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/300px-No_image_available.svg.png"
        listing = AuctionListing.objects.create(
            name=title, category=category, date=timezone.now(), startBid=start_bid, description=description, user=user,
            imageUrl=image_url, active=True)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/createListing.html", {
        'categories': Category.objects.all()
    })


def details(request, id):
    item = AuctionListing.objects.get(id=id)
    bids = Bid.objects.filter(auctionListing=item)
    comments = Comment.objects.filter(auctionListing=item)
    value = bids.aggregate(Max('bidValue'))['bidValue__max']
    bid = None
    if value is not None:
        bid = Bid.objects.filter(bidValue=value)[0]
    return render(request, "auctions/details.html", {
        'item': item,
        'bids': bids,
        'comments': comments,
        'bid': bid
    })


def categories(request):
    if request.method == 'POST':
        category = request.POST["category"]
        new_category, created = Category.objects.get_or_create(
            name=category.lower())
        if created:
            new_category.save()
        else:
            messages.warning(request, "Category already Exists!")
        return HttpResponseRedirect(reverse("categories"))
    return render(request, "auctions/categories.html", {
        'categories': Category.objects.all()
    })


def filter(request, name):
    category = Category.objects.get(name=name)
    obj = AuctionListing.objects.filter(category=category)
    return render(request, "auctions/index.html", {
        "objects": obj
    })


@login_required
def comment(request, id):
    if request.method == 'POST':
        auction_listing = AuctionListing.objects.get(id=id)
        user = request.user
        comment_value = request.POST["content"].strip()
        if comment_value != "":
            comment = Comment.objects.create(date=timezone.now(
            ), user=user, auctionListing=auction_listing, commentValue=comment_value)
            comment.save()
        return HttpResponseRedirect(reverse("details", kwargs={'id': id}))
    return HttpResponseRedirect(reverse("index"))


@login_required
def bid(request, id):
    if request.method == 'POST':
        auction_listing = AuctionListing.objects.get(id=id)
        bid_value = request.POST["bid"]
        args = Bid.objects.filter(auctionListing=auction_listing)
        value = args.aggregate(Max('bid_value'))['bidValue__max']
        if value is None:
            value = 0
        if float(bid_value) < auction_listing.startBid or float(bid_value) <= value:
            messages.warning(
                request, f'Bid Higher than: {max(value, auction_listing.startBid)}!')
            return HttpResponseRedirect(reverse("details", kwargs={'id': id}))
        user = request.user
        bid = Bid.objects.create(
            date=timezone.now(), user=user, bidValue=bid_value, auctionListing=auction_listing)
        bid.save()
    return HttpResponseRedirect(reverse("details", kwargs={'id': id}))


@login_required
def end(request, item_id):
    auction_listing = AuctionListing.objects.get(id=item_id)
    user = request.user
    if auction_listing.user == user:
        auction_listing.active = False
        auction_listing.save()
        messages.success(
            request, f'Auction for {auction_listing.name} successfully closed!')
    else:
        messages.info(
            request, 'You are not authorized to end this listing!')
    return HttpResponseRedirect(reverse("details", kwargs={'id': item_id}))
