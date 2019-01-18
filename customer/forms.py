from django import forms
from .models import Customer

#ENTER PHONE NUMBER FORM
class LoginForm(forms.Form):
    phone_number = forms.CharField()

#VERIFY OTP FORM
class VerifyOtpForm(forms.Form):
    otp_input = forms.CharField()

class RegisterCustomerForm(forms.ModelForm):
    #customer_phone = forms.CharField(disabled=True)
    def __init__(self, *args, **kwargs):
       super(RegisterCustomerForm, self).__init__(*args, **kwargs)
       self.fields['customer_phone'].widget.attrs['readonly'] = True

    class Meta:
        model = Customer
        fields = ('customer_name','customer_phone', 'customer_email', 'customer_address')