from django.contrib import admin
from django.urls import path
from . import views
from .views import ProductListView,OrderListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home" ),
    path('category/<str:category>',views.category,name='category'),
    path('cart',views.cart,name='cart'),
    path('cart-item',views.cart_item,name='cart-item'),
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

    path('<int:pk>/product-details',views.product_details,name='product-details'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('product-list', ProductListView.as_view(), name='product-list'),
    path('order-list', OrderListView.as_view(), name='order-list'),
    path('dashboard-overview', views.dashboard_overview, name='dashboard-overview'),
    path('piechart',views.piechart,name='piechart'),
    path('barchart',views.barchart,name='barchart'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
