from django.contrib import admin
from .models import Profile, Wine, Cart, Manufacturer

# Register your models here.


admin.site.register(Profile)
admin.site.register(Wine)
admin.site.register(Cart)
admin.site.register(Manufacturer)
