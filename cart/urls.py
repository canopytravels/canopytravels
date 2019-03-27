from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/<str:order_type>/<str:pickup>/<str:drop>/',
         views.cart_add,
         name='cart_add'),
    path('add_addons/<int:product_id>',
         views.cart_add_addons,
         name='cart_add_addons'),
    path('remove/<int:product_id>/',
         views.cart_remove,
         name='cart_remove'),
]