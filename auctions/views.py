from .models import Category, AuctionListing, Bid, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .forms import CreateAuctionListingForm


def auction_index(request):
    check_auctions_auto()
    auction_wines = AuctionListing.objects.filter(active=True)
    return render(request, "auctions/auction_index.html", {
        "auction_wines": auction_wines,
    })


def all_auction_listings(request):
    check_auctions_auto()
    auction_wines = AuctionListing.objects.all()
    return render(request, "auctions/auction_index.html", {
        "auction_wines": auction_wines
    })


def filter(request, name):
    category = Category.objects.get(name=name)
    obj = AuctionListing.objects.filter(category=category)
    return render(request, "auctions/auction_index.html", {
        "objects": obj
    })


@login_required
def create_listing(request):
    check_auctions_auto()
    form = CreateAuctionListingForm(request.POST, request.FILES)
    print(form)
    if request.method == "POST":
        if form.is_valid():
            name = request.POST["name"]
            description = request.POST["description"]
            start_bid = request.POST["start_bid"]
            category = Category.objects.get(id=request.POST["category"])
            if request.POST["comments_allowed"]:
                comments_allowed = request.POST["comments_allowed"]
            else:
                comments_allowed = False
            user = request.user
            image = request.FILES["image"]
            auction_period = request.POST["auction_period"]
            image_url = "https://infiror.eu/default.png"
            end_date = timezone.now() + timezone.timedelta(days=int(auction_period))
            listing = AuctionListing.objects.create(
                name=name,
                category=category,
                date=timezone.now(),
                start_bid=start_bid,
                max_bid=start_bid,
                description=description,
                user=user,
                image=image,
                image_url=image_url,
                active=True,
                comments_allowed=comments_allowed,
                auction_period=auction_period,
                end_date=end_date
            )
            listing.save()
        else:
            messages.warning(request, "Form is not valid, please doublecheck entered info!")
        return HttpResponseRedirect(reverse("auction_index"))
    return render(request, "auctions/create_listing.html", {
        "categories": Category.objects.all()
    })


def details(request, wine_id):
    check_auctions_auto()
    wine = AuctionListing.objects.get(id=wine_id)
    bids = Bid.objects.filter(auctionListing=wine)
    max_bid = Bid.objects.filter(auctionListing=wine).aggregate(Max("bid_value"))
    max_bid = max_bid["bid_value__max"]
    comments = Comment.objects.filter(auctionListing=wine)
    value = bids.aggregate(Max("bid_value"))["bid_value__max"]
    if wine.end_date:
        wine_end_date = wine.end_date + timezone.timedelta(days=wine.auction_period)
    else:
        wine_end_date = wine.date + timezone.timedelta(days=wine.auction_period)

    wine_bid = None
    if value is not None:
        wine_bid = Bid.objects.filter(bid_value=value)[0]
    return render(request, "auctions/details.html", {
        "wine": wine,
        "bids": bids,
        "comments": comments,
        "wine_bid": wine_bid,
        "max_bid": max_bid,
        "wine_end_date": wine_end_date,
    })


def categories(request):
    check_auctions_auto()
    if request.method == "POST":
        category = request.POST["category"]
        new_category, created = Category.objects.get_or_create(
            name=category.lower())
        if created:
            new_category.save()
        else:
            messages.warning(request, "Category already Exists!")
        return HttpResponseRedirect(reverse("categories"))
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.all()
    })


@login_required
def comment(request, wine_id):
    check_auctions_auto()
    if request.method == "POST":
        auction_listing = AuctionListing.objects.get(id=wine_id)
        user = request.user
        comment_value = request.POST["content"].strip()
        if comment_value != "":
            written_comment = Comment.objects.create(
                date=timezone.now(),
                user=user,
                auctionListing=auction_listing,
                commentValue=comment_value
            )
            written_comment.save()
        return HttpResponseRedirect(reverse("details", kwargs={"wine_id": wine_id}))
    return HttpResponseRedirect(reverse("auction_index"))


@login_required
def bid(request, wine_id):
    check_auctions_auto()
    if request.method == "POST":
        auction_listing = AuctionListing.objects.get(id=wine_id)
        if request.POST["bid"]:
            bid_value = request.POST["bid"]
        else:
            bid_value = 0
        args = Bid.objects.filter(auctionListing=auction_listing)
        value = args.aggregate(Max("bid_value"))["bid_value__max"]
        if value is None:
            value = 0
        if float(bid_value) < auction_listing.start_bid or float(bid_value) <= value:
            messages.warning(
                request, f"Bid Higher than: {max(value, auction_listing.start_bid)}!")
            return HttpResponseRedirect(reverse("details", kwargs={"wine_id": wine_id}))
        user = request.user
        save_bid = Bid.objects.create(
            date=timezone.now(),
            user=user,
            bid_value=bid_value,
            auctionListing=auction_listing
        )
        save_bid.save()
        auction_listing.max_bid = bid_value
        auction_listing.last_bidder = user.username
        if auction_listing.end_date:
            auction_listing.end_date = auction_listing.end_date + timedelta(hours=1)
        else:
            auction_listing.end_date = auction_listing.date + timedelta(hours=1)
        auction_listing.save()
    return HttpResponseRedirect(reverse("details", kwargs={"wine_id": wine_id}))


@login_required
def end(request, wine_id):
    check_auctions_auto()
    auction_listing = AuctionListing.objects.get(id=wine_id)
    user = request.user
    if auction_listing.user == user:
        auction_listing.active = False
        auction_listing.save()
        messages.success(
            request, f"Auction for {auction_listing.name} successfully closed!")
    else:
        messages.info(
            request, "You are not authorized to end this listing!"
        )
    return HttpResponseRedirect(reverse("details", kwargs={"wine_id": wine_id}))


def my_auction_listings(request):
    check_auctions_auto()
    auction_wines = AuctionListing.objects.filter(user=request.user).order_by("-active")
    return render(request, "auctions/auction_index.html", {
        "auction_wines": auction_wines
    })


def ended_auction_listings(request):
    check_auctions_auto()
    auction_wines = AuctionListing.objects.filter(active=False)
    return render(request, "auctions/auction_index.html", {
        "auction_wines": auction_wines
    })


def my_ended_auction_listings(request):
    check_auctions_auto()
    auction_wines = AuctionListing.objects.filter(user=request.user, active=False)
    return render(request, "auctions/auction_index.html", {
        "auction_wines": auction_wines
    })


def my_won_auction_listings(request):
    check_auctions_auto()
    auction_wines = AuctionListing.objects.filter(active=False, last_bidder=request.user)
    return render(request, "auctions/auction_index.html", {
        "auction_wines": auction_wines
    })


def check_auctions_auto():
    auctions_ending = AuctionListing.objects.filter(active=True)
    for auction in auctions_ending:
        if auction.end_date:
            if auction.end_date < timezone.now():
                auction.active = False
                auction.save()
                print(f"Auction for {auction.name} ended automatically! because {auction.end_date} < {timezone.now()}")
        if auction.date + timezone.timedelta(
                days=auction.auction_period
        ) < timezone.now():
            auction.active = False
            auction.save()
