
from django import forms
from django.forms import ModelForm
from .models import ShippingAddress


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields=['name','phone','address','city','postcode','country']