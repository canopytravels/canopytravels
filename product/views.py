from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from cart.forms import CartAddProductForm
from product.models import Product, Category, SubCategory

# Create your views here.
# def products(request):
#     return HttpResponse('Welcome to Product Page')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    cart_product_form = CartAddProductForm()

    return render(request,
                  'list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'cart_product_form': cart_product_form})

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