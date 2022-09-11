from django.contrib import admin

from .models import Manufacturer, Wine

admin.site.register(Wine)
admin.site.register(Manufacturer)
