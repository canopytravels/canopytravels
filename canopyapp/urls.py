from django.urls import path
from canopyapp import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('canopyadmin', views.canopyadmin, name='canopyadmin'),
    #path('test_view', views.index, name='test_view'),
    # path('login', views.user_login, name='login'),
    # path('verifyotp', views.verify_login, name='verifyotp'),
    # path('register_customer', views.register_customer, name='register_customer'),
    # path('products', ListView.as_view(
    #                                 queryset=Product.objects.all(),
    #                                 template_name="index.html")),

]