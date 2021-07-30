from django.shortcuts import render,redirect
from .models import Product,Cart,ShippingAddress,OrderItem,Order
from .forms import ShippingAddressForm
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
import json
import datetime


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
        product=Cart.objects.get(product__pk=product_id,user__pk=user_id)
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

def create_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user,transaction_id=transaction_id)
        cart_items = Cart.objects.filter(user=user)
        for item in cart_items:
            order_item = OrderItem(order=order,product=item.product,quantity=item.quantity)
            order_item.save()

        request.session['order_id'] = order.pk
        return redirect('shipping-address')

def shipping_address(request):
    order_id = request.session.get('order_id')
    order = Order.objects.get(pk=order_id) 
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.order = order
            obj.save()
            return redirect('payment')

    else:
        form = ShippingAddressForm()
    
    template_name="store/shipping.html"
    context={
        's_form':form,
        
    }
    return render(request, template_name,context)

def payment_view(request):
    user_id = request.user.id
    order_id = request.session.get('order_id')
    s_address = ShippingAddress.objects.get(order__pk=order_id)
    order_items = OrderItem.objects.filter(order__pk=order_id)
    context={
        'user_id':user_id,
        's_address':s_address,
        'order_items':order_items,
    }

    template_name = 'store/payment.html'
    return render(request, template_name,context)