import django.contrib.auth.decorators
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
from warket_viewer.models import Wine


@require_POST
def cart_add(request, wine_id):
    cart = Cart(request)
    wine = get_object_or_404(Wine, pk=wine_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        selected_wine = Wine.objects.get(pk=wine_id)
        if selected_wine.units_in_stock >= cd["quantity"]:
            cart.add(wine=wine, quantity=cd["quantity"], update_quantity=cd["update"])
        else:
            cart.add(wine=wine, quantity=selected_wine.units_in_stock, update_quantity=cd["update"])
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
def cart_clear(request):
    cart = Cart(request)
    print(cart.cart)
    if request.method == "POST":
        delete_from_cart = []
        for item in cart:
            wine_id = int(item["wine"].id)
            quantity = int(item["quantity"])
            print(quantity)
            wine_in_cart = Wine.objects.get(id=wine_id)
            delete_from_cart.append(wine_id)
            wine_in_cart.units_in_stock -= quantity
            wine_in_cart.save()
        for item in delete_from_cart:
            wine = get_object_or_404(Wine, pk=item)
            cart.remove(wine)
            messages.success(request, "Thank You for your purchase")
    return redirect("list_wines")
