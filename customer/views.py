from django.shortcuts import redirect, render, get_list_or_404
from customer.models import Customer
# from canopyapp.models import Product, ProductPrice, Booking
# from .forms import CategoryForm, SubCategoryForm, ChargeCategoryForm, ProductForm, ProductPriceForm, BookingForm

from django.http import HttpResponse
from .forms import LoginForm, VerifyOtpForm, RegisterCustomerForm

#for decorators
from django.views.decorators.http import require_http_methods

#for sending OTP
import http.client
import json

#for alert message
from django.contrib import messages

#************SELF DECLARED UTILITY METHODS****************
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

#SAVE logged in users instance
def save_loggedIn():
    request.session['loggedIn'] = "True"

#check user is logged in or not
def is_loggedIn():
    return request.session.get('loggedIn')


#**********************END************************************

#LOGIN IMPLEMENTATION
def user_login(request):
    is_loggedIn = request.session.get('loggedIn')
    phone = request.session.get('phone_number')
    if phone == None:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                phone_number = request.POST.get('phone_number')
                request.session['phone_number'] = phone_number
                #otp_data = send_otp(phone_number)
                otp_data = {'type':'success'}
                if otp_data['type']=='success':
                    return redirect('customer:verifyotp')
                    #return HttpResponse('Enter OTP: '+phone_number+'session: '+request.session.get('phone_number'))
                    #return render(request, 'verifyotp.html', {})
                else:
                    return HttpResponse('Invalid login')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})

    elif phone != None and is_loggedIn=="True":
        return redirect('product_list')

    else:
        del request.session['phone_number']
        return redirect('customer:login')

        # FOR DISPLAYING ALERT MESSAGE
        # messages.info(request, 'You are Already LoggedIn!')
        ##


#VERFITY OTP IMPLEMENTATION
def verify_login(request):
    phone = request.session.get('phone_number')
    if phone != None:
        if request.method == 'POST':
            form = VerifyOtpForm(request.POST)
            if form.is_valid():
                otp = request.POST.get('otp_input')
                #otp_data = verify_otp(phone, otp)
                otp_data = {'type':'success'}
                if otp_data['type']=='success':
                    if customer_exists(phone):
                        request.session['loggedIn'] = "True"
                        from_cart = request.session.get('from_cart')
                        #from_cart =True
                        if from_cart:
                            return redirect('orders:create')
                        else:
                            return HttpResponse('GOTO HOME PAGE')
                    else:
                        return redirect('customer:register_customer')
                else:
                    return HttpResponse('Invalid OTP')
        else:
            form = VerifyOtpForm()
        return render(request, 'verifyotp.html', {'form': form})
    else:
        return redirect('customer:login')


#REGISTRATION FORM IMPLEMENTATION
#@require_http_methods(["POST"])
def register_customer(request):
    phone = request.session.get('phone_number')
    if phone != None:
        if request.method == 'POST':
            form = RegisterCustomerForm(request.POST)
            if form.is_valid():
                customer = form.save(commit=False)
                customer.save()
                request.session['loggedIn'] = "True"
                from_cart = request.session.get('from_cart')
                if from_cart:
                    return redirect('orders:create')
                else:
                    return HttpResponse('GOTO HOME PAGE')

        else:
            data = {'customer_phone': phone}
            form = RegisterCustomerForm(initial=data)
        return render(request, 'register_customer.html', {'form': form})
    else:
        return redirect('customer:login')


#LOG OUT IMPLEMENTATION
def logout(request):
    phone = request.session.get('phone_number')
    is_loggedIn = request.session.get('loggedIn')
    if is_loggedIn != None and phone != None:
        del request.session['phone_number']
        del request.session['loggedIn']
        request.session.modified = True

        return redirect('customer:login')
    else:
        return redirect('customer:login')




