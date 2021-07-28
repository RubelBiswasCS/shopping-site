from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home" ),
    path('add-to-cart',views.add_to_cart,name="add-to-cart"),
    path('cart',views.cart,name='cart'),
]


