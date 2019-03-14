import datetime

from django import forms


DEFAULT = 'DF'
HOURLY = 'HR'
DAILY = 'DY'
WEEKLY = 'WK'
ORDER_TYPE_CHOICES = (
        (HOURLY, 'Hourly'),
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
    )


class ProductSearchForm(forms.Form):
    order_type = forms.ChoiceField(
        choices=ORDER_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': "form-control"}),
    )
    #pickup = forms.DateTimeField(widget=forms.SplitDateTimeWidget())
    # pickup = forms.DateTimeField(widget=DateInput())
    #drop = forms.DateTimeField()

    # pickup = forms.DateTimeField(
    #     input_formats=['%Y-%m-%d %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )

    # drop = forms.DateTimeField(
    #     input_formats=['%Y-%m-%d %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker2'
    #     })
    # )

    pickup = forms.DateTimeField()

    drop = forms.DateTimeField()

    # pickup = forms.DateTimeField(
    #     widget=DateTimePicker(
    #         options={
    #             'minDate': (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),  # Tomorrow
    #             'useCurrent': True,
    #             'collapse': False,
    #         },
    #         attrs={
    #           'append': 'fa fa-calendar',
    #           'input_toggle': False,
    #           'icon_toggle': True,
    #         }
    #     ),
    # )

    # drop = forms.DateTimeField(
    #     widget=DateTimePicker(
    #         options={
    #             # 'minDate': (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),  # Tomorrow
    #             # 'useCurrent': True,
    #             # 'collapse': False,
    #         },
    #         attrs={
    #           'append': 'fa fa-calendar',
    #         #   'input_toggle': False,
    #         #   'icon_toggle': True,
    #         }
    #     ),
    # )