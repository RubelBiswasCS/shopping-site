from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home" ),
    
    path('cart',views.cart,name='cart'),
    path('add-to-cart',views.add_to_cart,name="add-to-cart"),
    
    path('cart-action',views.cart_action,name="cart-action"),

    path('create-order',views.create_order,name="create-order"),
    path('shipping-address',views.shipping_address,name='shipping-address'),
    path('order-overview',views.order_overview,name='order-overview'),
    path('payment',views.payment_view,name='payment'),
    path('payment-method',views.payment_method,name='payment-method'),
    path('add-product',views.add_product,name='add-product'),
    path('update-product',views.update_product,name='update-product'),
    path('delete-product',views.delete_product,name='delete-product'),
    path('product-details',views.product_details,name='product-details'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
