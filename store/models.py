from django.db import models
from users.models import Profile

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
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(blank=True)
    completed = models.BooleanField(default=False)
