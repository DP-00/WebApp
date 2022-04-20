from django.http import Http404
from django.shortcuts import redirect, render
from yaml import serialize_all
from .models import *
from .forms import UserRegistrationForm, UserUpdateForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

import requests
from rest_framework import viewsets, status
from .serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


def index(request):
    comment = Comment.objects.filter(stars=5).order_by('?').first()
    cheapestBike = Product.objects.filter(category='Bike').all().aggregate(Min('price'))
    cheapestEBike = Product.objects.filter(category='E-bike').all().aggregate(Min('price'))
    personalizationPrice = Product.objects.filter(name='Personalization').all().aggregate(Min('price'))
    context = {'comment': comment, 'cheapestBike': cheapestBike, 'cheapestEBike':cheapestEBike, 'personalizationPrice':personalizationPrice}
    return render(request, 'KRRR/index.html', context)


def shop(request):
    products = requests.get("http://localhost:8000/api/shop")
    context = {'products': products}
    return render(request, 'KRRR/shop.html', context)

def product(request, id):
    product = Product.objects.get(id = id)
    # product = requests.get(f"http://localhost:8000/api/shop/{id}")
    comments = Comment.objects.filter(product=product)
    return render(request, 'KRRR/product.html', {'product': product, 'comments': comments})


def cart(request):
    context = {}
    return render(request, 'KRRR/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'KRRR/checkout.html', context)








class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    success_url = '/'
    template_name = 'KRRR/register.html'


class UserProfileView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'KRRR/customer.html'
    success_url = 'customer'



def adminAdmin(request):
    return render(request, 'KRRR/admin-admin.html', {})

def adminUsers(request):
    if request.method != "GET":
        raise Http404("Something went wrong")

    users = requests.get(f"http://localhost:8000/api/users/").json()
    return render(request, 'KRRR/admin-users.html', { "users": users })

    

def adminUserDetail(request, id):
    if request.method == "GET":
        user = requests.get(f"http://localhost:8000/api/users/{id}/").json()
    
    if request.method == "PUT":
        user = requests.put(f"http://localhost:8000/api/users/{id}/").json()
    
    
    return render(request, 'KRRR/admin-user.html', { "user": user })