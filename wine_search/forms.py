from django import forms


class WineSearchImageUpload(forms.Form):
    url = forms.URLField(label='URL')