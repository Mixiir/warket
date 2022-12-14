from django import forms

from .models import Category


class CreateAuctionListingForm(forms.Form):
    name = forms.CharField(
        label="name",
        max_length=50
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all()
    )
    description = forms.CharField(
        label="description",
        max_length=250
    )
    start_bid = forms.DecimalField(
        label="start_bid",
        decimal_places=2,
        max_digits=7
    )
    image = forms.ImageField(
        label="image_url",
        required=False
    )
    auction_period = forms.IntegerField(
        label="auction_period",
        min_value=1,
        max_value=30
    )
    comments_allowed = forms.BooleanField(
        label="comments_allowed",
        required=False
    )
