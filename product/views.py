from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from cart.forms import CartAddProductForm
from product.forms import ProductSearchForm
from product.models import Product, Category, SubCategory

#IMPORT FOR GETTING BOOKING HISTORY
from customer.models import Customer
from order.models import Order, OrderItem


# Create your views here.
# def products(request):
#     return HttpResponse('Welcome to Product Page')


def search(request):
    form = ProductSearchForm(request.POST)
    if form.is_valid():
        order_type = form.cleaned_data['order_type']
        pickup = request.POST.get('pickup')
        drop = request.POST.get('drop')
        request.session['order_type'] = order_type
        request.session['pickup'] = pickup
        request.session['drop'] = drop
        # return HttpResponse('Working: '+order_type)
        return redirect('product_list')
    else:
        return HttpResponse('Not Working')


def product_list(request, category_slug=None):
    # order_type = request.POST.get('ordertype')

    global order_type
    order_type = None
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    cart_product_form = CartAddProductForm()
    product_search_form = ProductSearchForm()

    # for retrieving search form values from sessions
    order_type = request.session.get('order_type')
    pickup = request.session.get('pickup')
    drop = request.session.get('drop')
    # END

    if order_type == None:
        order_type = "default"

    return render(request,
                  'list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'product_search_form': product_search_form,
                   'cart_product_form': cart_product_form,
                   'order_type':order_type,
                   'pickup': pickup,
                   'drop': drop})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'detail.html',
                  {'product': product})

#test method for checking user logged in or not (NEEDED to be implemented with booking button)
def check_login(request):
    is_loggedIn = request.session.get('loggedIn')
    if is_loggedIn == "True":
        return HttpResponse('User is currently logged in')
    else:
        return HttpResponse('User is currently not logged in')

#for booking history
def booking_history(request):
    is_loggedIn = request.session.get('loggedIn')
    phone_number = request.session.get('phone_number')
    if is_loggedIn == "True" and phone_number!=None:

        customer = Customer.objects.get(customer_phone=phone_number)
        orders = customer.customer_orders.all()
        for order_id in orders:
            order = Order.objects.get(id=order_id.id)
            order_items = order.order_orderitems.all()
        return render(request, 'booking_history.html', {'bookings': orders})

        # return HttpResponse('BOOKING HISTORY:'+order_items.count())

        # customer = Customer.objects.values_list('id', flat=True).get(customer_phone=phone_number)
        # customer = Customer.objects.filter(customer_phone="1111").values('id')
        # orders = Order.objects.filter(customer_id=customer).values('id')
        # for order_id in orders:
        #     orderitems[order_id] = OrderItem.objects.filter(order_id)
        # return HttpResponse('BOOKING HISTORY:'+orders)
    else:
        return HttpResponse('User is currently not logged in')