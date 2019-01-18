from django.urls import path
from product import views

urlpatterns = [
    path('products', views.products, name='products'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    # path('products', ListView.as_view(
    #                                 queryset=Product.objects.all(),
    #                                 template_name="index.html")),

]