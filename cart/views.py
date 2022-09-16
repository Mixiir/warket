import django.contrib.auth.decorators
from decouple import config
from django.contrib import messages
from django.core.mail import BadHeaderError
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from warket_viewer.models import Wine
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, wine_id):
    cart = Cart(request)
    wine = get_object_or_404(Wine, pk=wine_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        selected_wine = Wine.objects.get(pk=wine_id)
        if selected_wine.units_in_stock >= cd["quantity"]:
            cart.add(
                wine=wine,
                quantity=cd["quantity"],
                update_quantity=cd["update"]
            )
        else:
            cart.add(
                wine=wine,
                quantity=selected_wine.units_in_stock,
                update_quantity=cd["update"]
            )
        return redirect("cart:cart_detail")


def cart_remove(request, wine_id):
    cart = Cart(request)
    wine = get_object_or_404(Wine, pk=wine_id)
    cart.remove(wine)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item["update_quantity_form"] = CartAddProductForm(
            initial={
                "quantity": item["quantity"],
                "update": True
            }
        )
    return render(request, "cart/detail.html", {"cart": cart})


@require_POST
@login_required
def cart_clear(request):
    cart = Cart(request)
    if request.method == "POST":
        delete_from_cart = []
        for item in cart:
            wine_id = int(item["wine"].id)
            wine_in_cart = Wine.objects.get(id=wine_id)
            user = request.user
            if not user.first_name:
                user.first_name = "Anonymous"
            first_name = user.first_name
            if not user.last_name:
                user.last_name = "Anonymous last name"
            last_name = user.last_name
            wine_name = item["wine"].name
            quantity = int(item["quantity"])
            seller = item["wine"].user
            email = config("EMAIL_USER")
            receiver_email = seller.email
            delete_from_cart.append(wine_id)
            wine_in_cart.units_in_stock -= quantity
            wine_in_cart.save()
            # Sending email to the seller
            subject = f"Warket: Order from {first_name} {last_name}"
            message = f"You have sold {quantity} bottles of '{wine_name}'" \
                      f" to {first_name} {last_name}." \
                      f"Please make sure you send the wine to the buyer."
            try:
                send_mail(
                    subject,
                    message,
                    email,
                    [receiver_email],
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
        for item in delete_from_cart:
            wine = get_object_or_404(Wine, pk=item)
            cart.remove(wine)
        messages.success(request, "Thank You for your purchase")
        return redirect("cart:cart_detail")
