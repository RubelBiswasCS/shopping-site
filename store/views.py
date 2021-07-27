from django.shortcuts import render
from .models import Product
from django.http import JsonResponse,HttpResponse

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
    data={
        'user_id':1,
    }
    return HttpResponse(data)