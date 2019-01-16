from django.urls import path
from customer import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('verifyotp', views.verify_login, name='verifyotp'),
    path('register_customer', views.register_customer, name='register_customer'),
    # path('products', ListView.as_view(
    #                                 queryset=Product.objects.all(),
    #                                 template_name="index.html")),

]