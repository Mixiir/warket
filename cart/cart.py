from decimal import Decimal

from django.conf import settings
from django.contrib import messages

from warket_viewer.models import Wine


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        # Compare cart to wine list
        # If wine is not in cart, remove it from cart
        for items in list(cart):
            if Wine.objects.filter(id=items).exists():
                pass
            else:
                del cart[items]
                self.save()
                messages.error(
                    request,
                    "One or more items in your cart are no longer available."
                )

    def add(self, wine, quantity=1, update_quantity=False):
        wine_id = str(wine.id)
        if wine_id not in self.cart:
            self.cart[wine_id] = {
                "quantity": 0,
                "price": str(wine.price_per_unit)
            }
        if update_quantity:
            self.cart[wine_id]["quantity"] = quantity
        else:
            self.cart[wine_id]["quantity"] += quantity
        self.save()

    def save(self):
        self.session.modified = True
        self.session[settings.CART_SESSION_ID] = self.cart

    def remove(self, wine):
        wine_id = str(wine.id)
        if wine_id in self.cart:
            del self.cart[wine_id]
            self.save()

    def __iter__(self):
        wine_ids = self.cart.keys()
        wines = Wine.objects.filter(id__in=wine_ids)
        for wine in wines:
            self.cart[str(wine.id)]["wine"] = wine
        for item in self.cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item["price"]) * item["quantity"]
                   for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
