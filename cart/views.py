from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from product.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm, CartAddAddonsForm

@require_POST
def cart_add(request, product_id, order_type, pickup, drop):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 order_type = order_type,
                 pickup = pickup,
                 drop = drop,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

# CART METHOD FOR ADDING ADDONS
@require_POST
def cart_add_addons(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddAddonsForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_addons(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

# END OF CART METHOD FOR ADDING ADDONS

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    category = Category.objects.get(name="ADDONS")
    products = category.product_category.all()

    cart_addons_form = CartAddAddonsForm()
    # return render(request, 'cart_index.html', {'cart': cart, 'addons': products,})
    return render(request, 'cart_index.html', {'cart': cart, 'addons': products, 'cart_addons_form': cart_addons_form,})
