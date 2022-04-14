from django.shortcuts import redirect, render
from .models import *
from .forms import CustomerRegistrationModel, CustomerUpdateModel
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

import requests
from rest_framework import viewsets
from .serializers import ProductSerializer

from .forms import CartItemForm

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
    products = Product.objects.all()
    form = CartItemForm(request.POST or None)
    if request.method == 'POST':
        user = request.user
        if not Order.objects.filter(customer=user).exists():
            order = Order(customer=user)
        else:
            order = Order.objects.get(customer=user)
        item = CartItem.objects.create(order=order, product=Product.objects.get(id=form.data['product']), quantity=form.data['quantity'])
        item.save()

    context = {'products': products, 'form': form}
    
    return render(request, 'KRRR/shop.html', context)

def product(request, id):
    product = Product.objects.get(id = id)
    comments = Comment.objects.filter(product=product)
    return render(request, 'KRRR/product.html', {'product': product, 'comments': comments})

@login_required
def cart(request):
    user = request.user
    if not Order.objects.filter(customer=user).exists():
        order = Order(customer=user)
    else:
        order = Order.objects.get(customer=user)
    products = CartItem.objects.filter(order=order)
    form = CartItemForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'order': order, 
        'products': products,
        'form': form
        }
    return render(request, 'KRRR/cart.html', context)



def checkout(request):
    context = {}
    return render(request, 'KRRR/checkout.html', context)


def credits(request):
    context = {}
    return render(request, 'KRRR/credits.html', context)





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
    return render(request, 'KRRR/admin-users.html', { "users": User.objects.all() })