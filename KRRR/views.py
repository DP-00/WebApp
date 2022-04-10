from django.http import Http404
from django.shortcuts import redirect, render
from yaml import serialize_all
from .models import *
from .forms import CustomerRegistrationModel, CustomerUpdateModel
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

import requests
from rest_framework import viewsets, status
from .serializers import ProductSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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







def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationModel(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = CustomerRegistrationModel()
    return render(request, "KRRR/register.html", {'form':form})


@login_required
def customer(request):
    if request.method == "POST":
        updated_form = CustomerUpdateModel(request.POST, instance=request.user)
        if updated_form.is_valid():
            updated_form.save()
            return redirect("customer")
    else:
        updated_form = CustomerUpdateModel(instance=request.user)

    return render(request, "KRRR/customer.html", {'updated_form':updated_form})


def adminAdmin(request):
    return render(request, 'KRRR/admin-admin.html', {})

def adminUsers(request):
    if request.method != "GET":
        raise Http404("Something went wrong")

    users = requests.get(f"http://localhost:8000/api/users/").json()
    return render(request, 'KRRR/admin-users.html', { "users": users })

    

def adminUserDetail(request, id):
    user = requests.get(f"http://localhost:8000/api/users/{id}/").json()
    return render(request, 'KRRR/admin-user.html', { "user": user })