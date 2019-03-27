from datetime import datetime

from django import forms
from django.forms import ValidationError

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

    pickup = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'readonly': 'readonly'}))

    drop = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'readonly': 'readonly'}))



    # def clean_drop(self):
    #     drop = self.cleaned_data['drop']

    #     if drop == None:
    #         raise ValidationError('Domain of email is not valid')

    #     return drop

    # # this function will be used for the validation
    # def clean(self):

    #     # data from the form is fetched using super function
    #     super(ProductSearchForm, self).clean()

    #     # extract the username and text field from the data
    #     pickup = self.cleaned_data.get('pickup')
    #     drop = self.cleaned_data.get('drop')

    #     # conditions to be met for the username length
    #     if pickup == None:
    #         self._errors['pickup'] = self.error_class([
    #             'Please enter pickup date & time'])
    #     # if len(text) <10:
    #     #     self._errors['text'] = self.error_class([
    #     #         'Post Should Contain minimum 10 characters'])

    #     # return any errors if found
    #     return self.cleaned_data

    # def clean_drop(self):
    #     drop = self.cleaned_data['drop']
    #     unformat_today = datetime.today()
    #     str_today = unformat_today.strftime('%Y-%m-%d %H:%M')
    #     today = datetime.strptime(str_today, '%Y-%m-%d %H:%M')
    #     if today > drop:
    #         raise ValidationError("Please enter valid drop date")
    #     return drop

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