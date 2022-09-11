from django import forms

from .models import Wine


class CreateWineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = [
            "name",
            "image",
            "description",
            "vintage",
            "alcohol_content",
            "price_per_unit",
            "units_in_stock",
            "manufacturer",
            "type",
            # "variety"
        ]


class EditWineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = [
            "name",
            "image",
            "description",
            "vintage",
            "alcohol_content",
            "price_per_unit",
            "units_in_stock",
            "manufacturer",
            "type",
            # "variety"
        ]


class FormAPI(forms.Form):
    image = forms.ImageField(label="image")

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            if image.size > 32 * 1024 * 1024:
                raise forms.ValidationError("Image file too large ( > 32mb )")
            return image
        else:
            raise forms.ValidationError("Couldn't read uploaded image")
