from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=0, max_value=100)
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
