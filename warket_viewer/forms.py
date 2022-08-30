from django import forms
from .models import Wine


class CreateWineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = [
            'name',
            'image',
            'description',
            'vintage',
            'alcohol_content',
            'price_per_unit',
            'units_in_stock',
            'manufacturer',
            'type',
            'variety'
        ]


class EditWineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = [
            'name',
            'image',
            'description',
            'vintage',
            'alcohol_content',
            'price_per_unit',
            'units_in_stock',
            'manufacturer',
            'type',
            'variety'
        ]
