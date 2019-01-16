from django.shortcuts import redirect, render, get_list_or_404
from canopyapp.models import Product, Cart, Entry, Customer, ProductPrice
# from canopyapp.models import Product, ProductPrice, Booking
# from .forms import CategoryForm, SubCategoryForm, ChargeCategoryForm, ProductForm, ProductPriceForm, BookingForm

from django.http import HttpResponse
from .forms import LoginForm, VerifyOtpForm, RegisterCustomerForm

#for sending OTP
import http.client
import json

# OTP SEND METHOD
def send_otp(mobile):
    conn = http.client.HTTPConnection("api.msg91.com")
    payload = ""
    conn.request("POST", "/api/sendotp.php?template=&otp_length=&authkey=256624Ax2u15T0ke135c3c6465&message=&sender=&mobile="+mobile+"&otp=&otp_expiry=&email=", payload)
    res = conn.getresponse()
    data = res.read()
    data_str = data.decode("utf-8")
    data_json = json.loads(data_str)
    return data_json

# OTP VERIFY METHOD
def verify_otp(mobile, otp):
    conn = http.client.HTTPSConnection("api.msg91.com")
    payload = ""
    headers = { 'content-type': "application/x-www-form-urlencoded" }
    conn.request("POST", "/api/verifyRequestOTP.php?authkey=256624Ax2u15T0ke135c3c6465&mobile="+mobile+"&otp="+otp, payload, headers)
    res = conn.getresponse()
    data = res.read()
    data_str = data.decode("utf-8")
    data_json = json.loads(data_str)
    return data_json

#check customer exists method
def customer_exists(mobile):
    return Customer.objects.filter(customer_phone=mobile).exists()

#LOGIN IMPLEMENTATION
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = request.POST.get('phone_number')
            request.session['phone_number'] = phone_number
            #otp_data = send_otp(phone_number)
            otp_data = {'type':'success'}
            if otp_data['type']=='success':
                return redirect('verifyotp')
                #return HttpResponse('Enter OTP: '+phone_number+'session: '+request.session.get('phone_number'))
                #return render(request, 'verifyotp.html', {})
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

#VERFITY OTP IMPLEMENTATION
def verify_login(request):
    phone = request.session.get('phone_number')
    if request.method == 'POST':
        form = VerifyOtpForm(request.POST)
        if form.is_valid():
            otp = request.POST.get('otp_input')
            #otp_data = verify_otp(phone, otp)
            otp_data = {'type':'success'}
            if otp_data['type']=='success':
                if customer_exists(phone):
                    return HttpResponse('Customer already exists')
                else:
                    return redirect('register_customer')
            else:
                return HttpResponse('Invalid OTP')
    else:
        form = VerifyOtpForm()
    return render(request, 'verifyotp.html', {'form': form})


#REGISTRATION FORM IMPLEMENTATION
def register_customer(request):
    phone = request.session.get('phone_number')
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            html = "<h1>Success</h1>"
            return HttpResponse(html)
    else:
        data = {'customer_phone': phone}
        form = RegisterCustomerForm(initial=data)
    return render(request, 'register_customer.html', {'form': form})








# Create your views here.
def test_view(request):
    html = "<h1>Success</h1>"
    return HttpResponse(html)



def index(request):

    productprices = ProductPrice.objects.all()
    prodprice = ProductPrice.objects.get(product_id=1, charge_category_id=1)

    print("Dummy: ",prodprice.charge)


    #Blog.objects.filter(author=author).values_list('id', flat=True)

    # all_products = Product.objects.all().values_list('pk', flat=True)
    # num_cars = Product.objects.all().count()
    # context = { 'num_cars':num_cars, 'all_products':all_products,}

    # return render(request, 'index.html', context=context)

    # Based on the user who is making the request, grab the cart object
    #my_cart = Cart.objects.get_or_create(customer=None)
    c = Customer.objects.get(pk=1)
    my_cart, created = Cart.objects.get_or_create(customer=c)
    # Get entries in the cart
    #my_carts_current_entries = Entry.objects.filter(cart=my_cart)
    my_carts_current_entries = 1
    # Get a list of your products
    products = Product.objects.filter(product_category=16)

    if request.method == "POST":
        # Get the product's ID from the POST request.
        product_id = request.POST.get('product_id')
        #print("Product_id: ",product_id, flush=True)
        # Get the object using our unique primary key
        product_obj = Product.objects.get(pk=product_id)
        # Get the quantity of the product desired.
        product_quantity = request.POST.get('product_quantity')
        # Create the new Entry...this will update the cart on creation
        Entry.objects.create(cart=my_cart, product=product_obj, quantity=product_quantity)
        return HttpResponse('kudos')

    return render(request, 'index.html', {'my_cart': my_cart, 'my_carts_current_entries': my_carts_current_entries,
                                              'products': products, 'productprices':productprices})

def canopyadmin(request):
    html = "<h1>Success</h1>"
    return HttpResponse(html)

# def canopyadmin(request):
#     if request.method == "POST":
#         form_category = CategoryForm(request.POST)
#         if form_category.is_valid():
#             post = form_category.save(commit=False)
#             post.save()
#             html = "<h1>Success</h1>"
#             return HttpResponse(html)

#         form_sub_category = SubCategoryForm(request.POST)
#         if form_sub_category.is_valid():
#             post = form_sub_category.save(commit=False)
#             post.save()
#             html = "<h1>Success</h1>"
#             return HttpResponse(html)

#         form_charge_category = ChargeCategoryForm(request.POST)
#         if form_charge_category.is_valid():
#             post = form_charge_category.save(commit=False)
#             post.save()
#             html = "<h1>Success</h1>"
#             return HttpResponse(html)

#         form_product = ProductForm(request.POST)
#         if form_product.is_valid():
#             post = form_product.save(commit=False)
#             post.save()
#             html = "<h1>Success</h1>"
#             return HttpResponse(html)

#         form_product_price = ProductPriceForm(request.POST)
#         if form_product_price.is_valid():
#             post = form_product_price.save(commit=False)
#             post.save()
#             html = "<h1>Success</h1>"
#             return HttpResponse(html)

#         form_booking = BookingForm(request.POST)
#         if form_booking.is_valid():
#             post = form_booking.save(commit=False)
#             post.save()
#             html = "<h1>Success</h1>"
#             return HttpResponse(html)

#     else:
#         form_category = CategoryForm()
#         form_sub_category = SubCategoryForm()
#         form_charge_category = ChargeCategoryForm()
#         form_product = ProductForm()
#         form_product_price = ProductPriceForm()
#         form_booking = BookingForm()


#     return render(request, 'canopyadmin.html', {'form_category': form_category, 'form_sub_category': form_sub_category,
#                     'form_charge_category': form_charge_category, 'form_product': form_product, 'form_product_price': form_product_price,
#                     'form_booking': form_booking,})

