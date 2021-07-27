from django.shortcuts import render
from .models import Product
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
    data={
        'user_id':user_id,
        'product_id':product_id,
    }
    response = json.dumps(data)
    return HttpResponse(response)