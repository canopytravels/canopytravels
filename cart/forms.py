from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 8)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int,
                                initial=1,
                                widget=forms.HiddenInput)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class CartAddAddonsForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int,
                                initial=0)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)