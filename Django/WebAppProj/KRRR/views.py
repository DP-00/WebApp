from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'KRRR/index.html', context)

def shop(request):
    context = {}
    return render(request, 'KRRR/shop.html', context)

def cart(request):
    context = {}
    return render(request, 'KRRR/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'KRRR/checkout.html', context)