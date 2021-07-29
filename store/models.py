from django.db import models
from users.models import Profile
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.IntegerField(unique=True)
    category = models.CharField(max_length=100)
    unit_price = models.FloatField()
    current_stock = models.IntegerField()
    
    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    # date_created = models.DateTimeField(auto_now_add=True,blank=True)
    # date_modified = models.DateTimeField(blank=True)
    # completed = models.BooleanField(default=False)

    def __str__(self):
        obj_name = self.user.username +'_'+ self.product.product_name
        return obj_name

class ShippingAddress(models.Model):
    # fields=[user,name,phone,address,city,postcode,country]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200,null=False)
    phone = models.IntegerField(null=False)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    postcode = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=100,null=False)
	# date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address