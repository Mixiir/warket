from django.contrib import admin
from .models import Wine, Cart, Manufacturer

admin.site.register(Wine)
admin.site.register(Cart)
admin.site.register(Manufacturer)
