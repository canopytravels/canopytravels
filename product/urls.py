from django.urls import path
from product import views



urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),

    #TEST url for checking user loggin or not
    path(r'^checklogin/', views.check_login, name='check_login'),
    path('booking_history',views.booking_history, name='booking_history'),
    path('search',views.search, name='search'),

    # path('products', ListView.as_view(
    #                                 queryset=Product.objects.all(),
    #                                 template_name="index.html")),

]