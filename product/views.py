from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from cart.forms import CartAddProductForm
from product.models import Product

# Create your views here.
def products(request):
    return HttpResponse('Welcome to Product Page')

def product_detail(request, id):
    product = get_object_or_404(Product, id=id,
                                         available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})