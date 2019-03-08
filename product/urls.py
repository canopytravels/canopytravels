from django.urls import path
from product import views



urlpatterns = [
    path('product', views.product_list, name='product_list'),
    path('search/<slug:category_slug>/product', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),

    #TEST url for checking user loggin or not
    path(r'^checklogin/', views.check_login, name='check_login'),
    path('booking_history',views.booking_history, name='booking_history'),
    path('search/<slug:category_slug>/',views.search, name='search'),

    # path('products', ListView.as_view(
    #                                 queryset=Product.objects.all(),
    #                                 template_name="index.html")),

]