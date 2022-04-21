import email
from pyexpat import model
from attr import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from matplotlib.pyplot import cla
from .models import *


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'