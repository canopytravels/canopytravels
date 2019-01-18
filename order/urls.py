from django.urls import path
from order import views

urlpatterns = [
    path('orders', views.orders, name='orders'),
    # path('products', ListView.as_view(
    #                                 queryset=Product.objects.all(),
    #                                 template_name="index.html")),

]