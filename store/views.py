from django.shortcuts import render
from .models import Product, Cart
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
import json


def home(request):
    products = Product.objects.all()

    context={
        'products':products,
    }
    template_name = 'store/home.html'
    return render(request, template_name,context)

# Create your views here.
def add_to_cart(request):
    user_id = request.POST['user_id']
    product_id = request.POST['product_id']
    if request.method=='POST':
        product=Product.objects.get(pk=product_id)
        user = User.objects.get(pk=user_id)
        
        cart_item = Cart(product=product,user=user)
        cart_item.save()
    data={
        'user_id':user_id,
        'product_id':product_id,
    }
    response = json.dumps(data)
    return HttpResponse(response)

def cart(request):
    user_id = request.POST['user_id']

    user = User.objects.get(pk=user_id)
    cart_items = Cart.objects.first().product.product_name

    data={
        
        'cart_items':cart_items,
    }

    response = json.dumps(data)
    return HttpResponse(response)      