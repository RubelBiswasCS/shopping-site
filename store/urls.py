from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home" ),
    
    path('cart',views.cart,name='cart'),
    path('add-to-cart',views.add_to_cart,name="add-to-cart"),
    path('remove-cart-item',views.remove_cart_item,name="remove-cart-item"),
    path('create-order',views.create_order,name="create-order"),
    path('shipping-address',views.shipping_address,name='shipping-address'),
    path('order-overview',views.order_overview,name='order-overview'),
    path('payment',views.payment_view,name='payment'),
    path('payment-method',views.payment_method,name='payment-method'),
]


