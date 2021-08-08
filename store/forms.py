from django import forms
from django.forms import ModelForm
from .models import ShippingAddress,Product


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields=['name','phone','address','city','postcode','country']

class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields=['product_name','product_code','category','unit_price','current_stock']