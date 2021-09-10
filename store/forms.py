from django import forms
from django.forms import ModelForm
from .models import ShippingAddress,Product,ProductImages


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields=['name','phone','address','city','postcode','country']

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields=['product_name','product_code','category','unit_price','current_stock']

class UpdateProductForm(ModelForm):
    class Meta:
        model = Product
        # fields=['product_name','product_code','category','unit_price','current_stock','product_img']
        fields=['product_name','product_code','category','unit_price','current_stock']

class AddProductImagesForm(ModelForm):
    class Meta:
        model = ProductImages
        fields = ['image',]        
