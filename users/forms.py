from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput


class UserRegisterForm(UserCreationForm):
    email =forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=EmailInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Retype Password'}))
class MyAuthForm(AuthenticationForm):
    
    # username= forms.CharField(widget=forms.TextInput, label='')
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password','label' : ''}))