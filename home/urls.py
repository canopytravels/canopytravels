from django.urls import path
from home import views



urlpatterns = [
    path('', views.index, name='index'),
    path('rent', views.rent, name='rent'),
]