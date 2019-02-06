from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.shortcuts import render, redirect
from django.http import HttpResponse
from customer.models import Customer
# from customer.views import customer

# Create your views here.
def orders(request):
    return HttpResponse('Welcome to ORDER Page')

def	order_create(request):
    cart	=	Cart(request)
    # if	request.method	==	'POST':
        # form	=	OrderCreateForm(request.POST)
        # if	form.is_valid():
        #     order	=	form.save()
        #     for	item	in	cart:
        #         OrderItem.objects.create(order=order, product=item['product'],price=item['price'], quantity=item['quantity'],
        #                                     order_type=item['order_type'], pickupdatetime=item['pickup'], dropdatetime=item['drop'])
        #     #	clear	the	cart
        #     cart.clear()
        #     return	render(request, 'created.html', {'order':	order})
    # else:
        # form	=	OrderCreateForm()
    return	render(request, 'create.html', {'cart':	cart})

def order_save(request):
    is_loggedIn = request.session.get('loggedIn')
    phone = request.session.get('phone_number')
    if is_loggedIn == "True":
        cart	=	Cart(request)
        if customer_exists(phone) and len(cart)>0:
            customer = Customer.objects.get(customer_phone=phone)
            order = Order.objects.create(customer=customer)

            for	item	in	cart:
                OrderItem.objects.create(order=order, product=item['product'],price=item['price'], quantity=item['quantity'],
                                            order_type=item['order_type'], pickupdatetime=item['pickup'], dropdatetime=item['drop'])
            #	clear	the	cart
            cart.clear()
            clear_search_values(request)
            return	render(request, 'created.html', {'order':	order})
        else:
            return HttpResponse('Unable to place your order!')
    else:
        # return HttpResponse('User is currently not logged in')
        request.session['from_cart'] = True
        return redirect('customer:login')






# def order_save(request):
#     cart	=	Cart(request)
#     if customer_exists('12345') and len(cart)>0:
#         customer = Customer.objects.get(customer_phone='12345')
#         order = Order.objects.create(customer=customer)

#         for	item	in	cart:
#             OrderItem.objects.create(order=order, product=item['product'],price=item['price'], quantity=item['quantity'],
#                                             order_type=item['order_type'], pickupdatetime=item['pickup'], dropdatetime=item['drop'])
#             #	clear	the	cart
#         cart.clear()
#         clear_search_values(request)
#         return	render(request, 'created.html', {'order':	order})

#     else:
#         return HttpResponse('Unable to place your order!')


#clear order_type, pickup and drop session values
def clear_search_values(request):
    del request.session['order_type']
    del request.session['pickup']
    del request.session['drop']
    if 'from_cart' in request.session:
        del request.session['from_cart']


#check customer exists method
def customer_exists(mobile):
    return Customer.objects.filter(customer_phone=mobile).exists()