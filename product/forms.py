from django import forms

DEFAULT = 'DF'
HOURLY = 'HR'
DAILY = 'DY'
WEEKLY = 'WK'
ORDER_TYPE_CHOICES = (
        (DEFAULT, 'Default'),
        (HOURLY, 'Hourly'),
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
    )

class ProductSearchForm(forms.Form):
    order_type = forms.ChoiceField(
        choices=ORDER_TYPE_CHOICES
    )
    pickup = forms.DateTimeField()
    drop = forms.DateTimeField()