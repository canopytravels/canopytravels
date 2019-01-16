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
    class Meta:
        model = Customer
        fields = ('customer_name','customer_phone', 'customer_email', 'customer_address')



#from .models import Category, SubCategory, ChargeCategory, Product, ProductPrice, Booking

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ('category_name',)

# class SubCategoryForm(forms.ModelForm):
#     class Meta:
#         model = SubCategory
#         fields = ('sub_category_name',)

# class ChargeCategoryForm(forms.ModelForm):
#     class Meta:
#         model = ChargeCategory
#         fields = ('charge_category_name',)

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('product_name', 'product_category', 'product_subcategory', 'product_image', 'product_description')

# class ProductPriceForm(forms.ModelForm):
#     class Meta:
#         model = ProductPrice
#         fields = ('charge_category_id', 'product_id', 'charge')

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ('booking_id', 'customer_id', 'product_id', 'quantity_booked', 'booking_type', 'datetime_from', 'datetime_to',)
