import email
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer



class CustomerRegistrationModel(UserCreationForm):
    email = forms.EmailField()
    nickname = forms.CharField(max_length=50)

    class Meta():
        model = Customer
        fields = ['name','surname','nickname','email','password1','password2']


class CustomerRegistrationModel(forms.ModelForm):
    email = forms.EmailField()
    nickname = forms.CharField(max_length=50)

    class Meta():
        model = Customer
        fields = ['name','surname','nickname','email']