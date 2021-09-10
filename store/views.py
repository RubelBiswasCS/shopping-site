from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Cart,ShippingAddress,OrderItem,Order,ProductImages
from .forms import ShippingAddressForm,AddProductForm,UpdateProductForm,AddProductImagesForm
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
import json
import datetime

from django.views.generic.list import ListView

from django.forms import modelformset_factory


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
    ImagesFormset = modelformset_factory(ProductImages,fields=['image',], extra=2)
    if request.method == 'POST':
        p_form = AddProductForm(request.POST)
        formset = ImagesFormset(request.POST,request.FILES)
        if p_form.is_valid() and formset.is_valid():
            p_form.save()
            product_code = p_form.cleaned_data['product_code']
            product = Product.objects.get(product_code=product_code)
            for form in formset:
                photo = form.cleaned_data['image']
                p_image = ProductImages(product=product,image=photo)
                p_image.save()
    else:
        p_form = AddProductForm()
        formset = ImagesFormset()
    context={
        'p_form':p_form,
        'formset':formset,
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
    product = Product.objects.get(pk=14)
    context={
        'product':product,
    }
    return render(request, template_name,context)

def delete_product(request):
    return HttpResponse("Product")
# Create your views here.
def add_to_cart(request):
    user_id = request.user.id
    product_id = request.POST['product_id']
    quantity=1
    # test_quantity = request.POST['quantity']
    # quantity=int(test_quantity)
    if request.POST['quantity']:
        quantity = request.POST['quantity']
        quantity = int(quantity)
    # if int(request.POST['quantity']) > 0:
    #     quantity = request.POST['quantity']
    #     quantity = int(quantity)
       
    if request.method=='POST':
        product=Product.objects.get(pk=product_id)
        user = User.objects.get(pk=user_id)
        try:
            existing_quantity=Cart.objects.get(user__pk=user_id,product=product).quantity
        except:
            existing_quantity=0 
        # cart_item = Cart(product=product,user=user,quantity=quantity)
        # cart_item.save()
        obj, created = Cart.objects.update_or_create(
    product=product, user=user,
    defaults={'quantity': existing_quantity+quantity},
)
    data={
        'user_id':user_id,
        'product_id':product_id,
        'product_qty': quantity,
    }
    # data ={}
    response = json.dumps(data)
    return HttpResponse(response)

#remove cart item
# def remove_cart_item(request):
#     user_id = request.POST['user_id']
#     product_id = request.POST['product_id']
#     # cart_user_id = Cart.objects.get(user__user_id = user_id)
#     if request.method=='POST' :
#         product=Cart.objects.get(product__pk=product_id,user__pk=user_id)
#         product.delete()
    
#     return HttpResponse("item deleted")

def cart_action(request):
    # user_id = request.POST['user_id']
    user_id = request.user.id
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
        elif action == 'remove':
            product.delete()
        else:
            pass
        # product.delete()
    response=user_id
    return HttpResponse(response)

def cart(request):
    user_id = request.user.id

    # user = User.objects.get(pk=1)
    
    # cart_items = Cart.objects.filter(user=user)
    if request.method == 'POST' :
        cart_items = Cart.objects.filter(user=request.user)
    items={}
    i=0
    total_price = 0
    for item in cart_items:
        if item.product.product_img:
            price = item.quantity * item.product.unit_price
            total_price += price
            items[i]={
                'product_id': item.product.pk,
                'product_name' :item.product.product_name,
                'unit_price' :item.product.unit_price,
                'quantity': item.quantity,
                'image':item.product.product_img.url,
                'price': price,
            }
        else:
            items[i]={
                'product_id': item.product.pk,
                'product_name' :item.product.product_name,
                'unit_price' :item.product.unit_price,
                'quantity': item.quantity,
               'price': price,
            }    
                
        
        i+=1
    data = items
    data = [total_price,items]
    # items=[]
    # for i in cart_items:
    #     items.append(i.product.product_name)
    # data={
        
    #     'cart_items':items,
    # }

    response = json.dumps(data)
    return HttpResponse(response)

def cart_item(request):
    template_name = 'store/cart.html'
    return render(request ,template_name)

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

def dashboard(request):
    template_name = 'store/dashboard.html'
    return render(request, template_name)

class ProductListView(ListView):
    model = Product
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

class OrderListView(ListView):
    model = Order
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context

def dashboard_overview(request):
    template_name = 'store/dashboard_overview.html'
    recent_orders = Order.objects.all()[0:5]
    top_products = Product.objects.all()[0:5]
    context = {
        'recent_orders' : recent_orders,
        'top_products' : top_products,
    }

    return render(request,template_name,context)


from .utils import draw_piechart,draw_barchart
# # Pie Chart
def piechart(request):
    products = Product.objects.all()
    draw_piechart(products)
    return render(request,'store/piechart.html')


def barchart(request):
    draw_barchart()
    return render(request,'store/barchart.html')
    
