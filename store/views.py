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
        try:
            quantity=Cart.objects.get(user__pk=user_id,product=product).quantity
        except:
            quantity=0    
        # cart_item = Cart(product=product,user=user,quantity=quantity)
        # cart_item.save()
        obj, created = Cart.objects.update_or_create(
    product=product, user=user,
    defaults={'quantity': quantity+1},
)
    data={
        'user_id':user_id,
        'product_id':product_id,
    }
    response = json.dumps(data)
    return HttpResponse(response)

#remove cart item
def remove_cart_item(request):
    user_id = request.POST['user_id']
    product_id = request.POST['product_id']
    # cart_user_id = Cart.objects.get(user__user_id = user_id)
    if request.method=='POST' :
        product=Cart.objects.get(product__pk=product_id)
        product.delete()
    
    return HttpResponse("item deleted")

def cart(request):
    user_id = request.POST['user_id']

    user = User.objects.get(pk=user_id)
    # cart_items = Cart.objects.filter(user=user)
    if request.method == 'POST' :
        cart_items = Cart.objects.filter(user=user)
    items={}
    i=0
    for item in cart_items:
        
        items[i]={
            'product_id': item.product.pk,
            'product_name' :item.product.product_name,
            'price' :item.product.unit_price,
            'quantity': item.quantity,
        }
            
        
        i+=1
    data = items
    # items=[]
    # for i in cart_items:
    #     items.append(i.product.product_name)
    # data={
        
    #     'cart_items':items,
    # }

    response = json.dumps(data)
    return HttpResponse(response)      