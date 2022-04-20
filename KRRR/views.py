from turtle import mode
from attr import fields
from django.http import Http404
from django.shortcuts import redirect, render
from yaml import serialize_all
from .models import *
from .forms import UserRegistrationForm, UserUpdateForm
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

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
    success_url = reverse_lazy('index')



def adminAdmin(request):
    return render(request, 'KRRR/admin-admin.html', {})

class AdminUsersView(ListView):
    model = User
    template_name = 'KRRR/admin-users.html'
    context_object_name = 'users'
    paginate_by = 5


class AdminUserView(DetailView):
    model = User
    template_name = 'KRRR/admin-user.html'
    context_object_name = 'user'