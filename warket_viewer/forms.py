from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from .models import Wine


class CreateWineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ['name', 'image', 'description', 'vintage', 'alcohol_content', 'price_per_unit',
                  'units_in_stock', 'manufacturer', 'type', 'variety']


class EditWineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ['name', 'image', 'description', 'vintage', 'alcohol_content', 'price_per_unit',
                  'units_in_stock', 'manufacturer', 'type', 'variety']
