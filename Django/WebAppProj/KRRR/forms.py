import email
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CartItem, Order

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = [
            'product',
            'quantity'
        ]
        labels = {
            'product': ''
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'location'
        ]
        widgets = {
            'location': forms.Select(attrs={'onchange': 'submit();'})
        }

class CustomerRegistrationModel(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta():
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class CustomerUpdateModel(forms.ModelForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta():
        model = User
        fields = ['first_name','last_name','username','email']