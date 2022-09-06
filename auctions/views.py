from .models import Category, AuctionListing, Bid, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

# TODO clean up the mess ...

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
def createListing(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST["title"]
        description = request.POST["description"]
        startBid = request.POST["startBid"]
        category = Category.objects.get(id=request.POST["category"])
        if request.POST['commentsAllowed']:
            commentsAllowed = request.POST["commentsAllowed"]
#            return commentsAllowed
        else:
            commentsAllowed=False
#            return commentsAllowed
#       print(request.POST["commentsAllowed"])
        user = request.user
        imageUrl = request.POST["url"]
        if imageUrl == '':
            imageUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/300px-No_image_available.svg.png"
# TODO  split the rows
        listing = AuctionListing.objects.create(
            name=title, category=category, date=timezone.now(), startBid=startBid, description=description, user=user,
            imageUrl=imageUrl, active=True, commentsAllowed=commentsAllowed,)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/createListing.html", {
        'categories': Category.objects.all()
    })

# TODO do not use id use it longer

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
        bidValue = request.POST["bid"]
        args = Bid.objects.filter(auctionListing=auction_listing)
        value = args.aggregate(Max('bidValue'))['bidValue__max']
        if value is None:
            value = 0
        if float(bidValue) < auction_listing.startBid or float(bidValue) <= value:
            messages.warning(
                request, f'Bid Higher than: {max(value, auction_listing.startBid)}!')
            return HttpResponseRedirect(reverse("details", kwargs={'id': id}))
        user = request.user
        bid = Bid.objects.create(
            date=timezone.now(), user=user, bidValue=bidValue, auctionListing=auction_listing)
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
