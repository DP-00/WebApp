import email
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

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

class UserOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'location',
            'order_date'
        ]
        widgets = {
            'location': forms.Select(),
            'order_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'stars',
            'content'
        ]
        labels = {
            'stars': 'Your opinion',
            'content': 'Describe your experience'
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta():
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta():
        model = User
        fields = ['first_name','last_name','username','email']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'