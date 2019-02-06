from django.urls import path
from order import views

app_name = "orders"

urlpatterns = [
    path('orders', views.orders, name='orders'),
    path('create/', views.order_create, name='create'),
    path('create/save', views.order_save, name='order_save'),
    # path('products', ListView.as_view(
    #                                 queryset=Product.objects.all(),
    #                                 template_name="index.html")),

]