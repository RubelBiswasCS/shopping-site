from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Cart,ShippingAddress,OrderItem,Order
from .forms import ShippingAddressForm,AddProductForm,UpdateProductForm
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

#add product view
def add_product(request):
    template_name = 'store/add_product.html'
    
    if request.method == 'POST':
        p_form = AddProductForm(request.POST,request.FILES)
        if p_form.is_valid():
            p_form.save()
    else:
        p_form = AddProductForm()
    context={
        'p_form':p_form,
    }
    return render(request, template_name,context)

# update product view
def update_product(request):
    template_name = 'store/update_product.html'
    instance = Product.objects.get(product_code=1001)
    if request.method == 'POST':
        u_p_form = UpdateProductForm(request.POST,request.FILES)
        if u_p_form.is_valid():
            u_p_form.save()
    else:
        u_p_form = UpdateProductForm(instance=instance)
    context={
        'u_p_form':u_p_form,
    }
   
    return render(request, template_name,context)

# product details view
def product_details(request):
    template_name = 'store/product_details.html'
    product = Product.objects.get(pk=5)
    context={
        'product':product,
    }
    return render(request, template_name,context)

def delete_product(request):
    return HttpResponse("Product")
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

def cart_action(request):
    user_id = request.POST['user_id']
    product_id = request.POST['product_id']
    action = request.POST['action']
    # cart_user_id = Cart.objects.get(user__user_id = user_id)
    if request.method=='POST' :
        product=Cart.objects.get(product__pk=product_id,user__pk=user_id)
        if action == '+':
            product.quantity+=1
            product.save()
        elif action == '-':
            
            product.quantity-=1
            if product.quantity <= 0:
                product.delete()
            else:
                product.save()
        else:
            pass
        # product.delete()
    response=action
    return HttpResponse(response)

def cart(request):
    user_id = request.POST['user_id']

    user = User.objects.get(pk=user_id)
    # cart_items = Cart.objects.filter(user=user)
    if request.method == 'POST' :
        cart_items = Cart.objects.filter(user=user)
    items={}
    i=0
    for item in cart_items:
        if item.product.product_img:

            items[i]={
                'product_id': item.product.pk,
                'product_name' :item.product.product_name,
                'unit_price' :item.product.unit_price,
                'quantity': item.quantity,
                'image':item.product.product_img.url,
            }
        else:
            items[i]={
                'product_id': item.product.pk,
                'product_name' :item.product.product_name,
                'unit_price' :item.product.unit_price,
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


def shipping_address(request):
    # order_id = request.session.get('order_id')
    # order = Order.objects.get(pk=order_id)
    request.session['temp_order_id'] = datetime.datetime.now().timestamp()
    initial = get_object_or_404(ShippingAddress, user = request.user)
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            postcode = form.cleaned_data['postcode']
            country = form.cleaned_data['country']
            obj, created = ShippingAddress.objects.update_or_create(
    user=request.user,
    defaults={'name':name,'phone':phone,'address':address,'city':city,'postcode':postcode,'country':country},
)
            obj.user = request.user
            obj.save()
            # obj = form.save(commit=False)
            # obj.user = request.user
            # # obj.order = order
            # obj.save()
            return redirect('payment')

    else:
        form = ShippingAddressForm(instance=initial)
    
    template_name="store/shipping.html"
    context={
        's_form':form,
        
    }
    return render(request, template_name,context)

def payment_view(request):
    user_id = request.user.id
    # order_id = request.session.get('order_id')
    # order_id = 14
    # s_informations = ShippingAddress.objects.get(order__pk=order_id)
    # order_items = OrderItem.objects.filter(order__pk=order_id)
    context={
        'user_id':user_id,
        # 's_informations':s_informations,
        # 'order_items':order_items,
    }

    template_name = 'store/payment.html'
    return render(request, template_name,context)


def payment_method(request):
    template_name = 'store/payment_method.html'
    return render(request, template_name)

def create_order(request):
    temp_order_id = request.session.get('temp_order_id')
    transaction_id = datetime.datetime.now().timestamp()
    
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(temp_order_id=temp_order_id,user=user)
        
        cart_items = Cart.objects.filter(user=user)
        for item in cart_items:
            order_item, created = OrderItem.objects.get_or_create(order=order,product=item.product,quantity=item.quantity)
            item.delete()
            # order_item = OrderItem(order=order,product=item.product,quantity=item.quantity)
            # order_item.save()
        order.transaction_id=transaction_id
        order.save()
        request.session['order_id'] = order.pk
        return redirect('order-overview')

def order_overview(request):
    user_id = request.user.id
    order_id = request.session.get('order_id')

    order = Order.objects.get(pk=order_id)
    shipping_address = ShippingAddress.objects.get(user__pk=user_id)
    order_items = OrderItem.objects.filter(order__pk=order_id)

    context={
        'order': order,
        'shipping_address':shipping_address,
        'order_items': order_items,
    }
    template_name = 'store/order_details.html'
    return render(request, template_name,context)
