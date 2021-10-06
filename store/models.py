from django.db import models
from users.models import Profile
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    # product_name,product_code,category,unit_price,current_stock
    product_name = models.CharField(max_length=100)
    product_code = models.IntegerField(unique=True)
    category = models.CharField(max_length=100)
    unit_price = models.FloatField()
    current_stock = models.IntegerField()

    def __str__(self):
        return self.product_name
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/',blank=True, default="no-product-image.png")

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    # date_created = models.DateTimeField(auto_now_add=True,blank=True)
    # date_modified = models.DateTimeField(blank=True)
    # completed = models.BooleanField(default=False)

    def __str__(self):
        obj_name = self.user.username
        return obj_name

    # @property
    # def get_total_item(self):
    #     cartitems = self.product_set.all()
    #     total = sum([item.get_total for item in orderitems])
    #     return total



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	# date_ordered = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=100,default="incomplete")
    transaction_id = models.CharField(max_length=100, null=True)
    temp_order_id = models.CharField(max_length=100, null=True)
    
    
    def __str__(self):
        return str(self.user.username)


	# @property
	# def get_cart_total(self):
	# 	orderitems = self.orderitem_set.all()
	# 	total = sum([item.get_total for item in orderitems])
	# 	return total


class ShippingAddress(models.Model):
    # fields=[user,name,phone,address,city,postcode,country]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200,null=False)
    phone = models.IntegerField(null=False)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    postcode = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=100,null=False)
	# date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
	# date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total = self.product.unit_price * self.quantity
        return total
class PaymentMethod(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    method = models.CharField(max_length=100,null=False)
