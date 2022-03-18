from django.shortcuts import render
from .models import *


def index(request):
    context = {}
    return render(request, 'KRRR/index.html', context)


def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'KRRR/shop.html', context)


def cart(request):
    context = {}
    return render(request, 'KRRR/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'KRRR/checkout.html', context)
