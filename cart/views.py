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
        cart.add(wine=wine, quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect('cart:cart_detail')


def cart_remove(request, wine_id):
    cart = Cart(request)
    wine = get_object_or_404(Wine, pk=wine_id)
    cart.remove(wine)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial=
                                                          {'quantity': item['quantity'],
                                                           'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
