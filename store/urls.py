from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home" ),
    
    path('cart',views.cart,name='cart'),
    path('add-to-cart',views.add_to_cart,name="add-to-cart"),
    path('remove-cart-item',views.remove_cart_item,name="remove-cart-item"),
]


