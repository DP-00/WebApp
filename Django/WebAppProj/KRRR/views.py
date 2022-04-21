from django.shortcuts import redirect, render
from .models import *
from .forms import CustomerRegistrationModel, CustomerUpdateModel
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

import requests
from rest_framework import viewsets
from .serializers import ProductSerializer

from .forms import CartItemForm, OrderForm, CommentEditForm

from django.db.models import Sum


#  index - main page
def index(request):
    comment = Comment.objects.filter(stars=5).order_by('?').first()
    cheapestBike = Product.objects.filter(category='Bike').all().aggregate(Min('price'))
    cheapestEBike = Product.objects.filter(category='E-bike').all().aggregate(Min('price'))
    personalizationPrice = Product.objects.filter(name='Personalization').all().aggregate(Min('price'))
    context = {'comment': comment, 'cheapestBike': cheapestBike, 'cheapestEBike':cheapestEBike, 'personalizationPrice':personalizationPrice}
    return render(request, 'KRRR/index.html', context)


# API
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


# shopping
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

    context = {
        'products': products, 
        'form': form
        }
    return render(request, 'KRRR/shop.html', context)


def product(request, id):
    form = CartItemForm(request.POST or None)
    if request.method == 'POST':
        user = request.user
        if not Order.objects.filter(customer=user, status='cart').exists():
            order = Order(customer=user, status='cart')
            order.save()
        else:
            order = Order.objects.get(customer=user, status='cart')

        if not CartItem.objects.filter(order=order, product=Product.objects.get(id=id)).exists():
            item = CartItem.objects.create(order=order, product=Product.objects.get(id=id), quantity=form.data['quantity'])
        else:
            item = CartItem.objects.get(order=order, product=Product.objects.get(id=id))
            quantity = item.quantity + int(form.data['quantity'])
            item.quantity = quantity
        item.save()

    product = Product.objects.get(id = id)
    comments = Comment.objects.filter(product=product)
    context = {
        'product': product, 
        'comments': comments, 
        'form': form
    }
    return render(request, 'KRRR/product.html', context)

@login_required
def cart(request):
    user = request.user
    if not Order.objects.filter(customer=user, status='cart').exists():
        order = Order(customer=user, status='cart')
        order.save()
    else:
        order = Order.objects.get(customer=user, status='cart')
    products = CartItem.objects.filter(order=order)
    form = OrderForm(request.POST or None)
    if request.method == 'POST':
        order.location = form.data['location']
        order.order_date = form.data['order_date']
        order.save()

    cart_total = sum([product.product.price*product.quantity for product in products])
    cart_quantity = sum([product.quantity for product in products])
    context = {
        'order': order, 
        'products': products,
        'form': form,
        'cart_total': cart_total,
        'cart_quantity' : cart_quantity
        }
    return render(request, 'KRRR/cart.html', context)


def checkout(request):
    order = Order.objects.get(customer=request.user, status='cart')
    products = CartItem.objects.filter(order=order)
    cart_total = sum([product.product.price*product.quantity for product in products])
    cart_quantity = sum([product.quantity for product in products])
    order.status = 'paid'
    order.save()

    context = {
        'products': products,
        'cart_total': cart_total,
        'cart_quantity' : cart_quantity,
        }
    return render(request, 'KRRR/checkout.html', context)


# customer and account management
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
def account(request):
    orders = Order.objects.filter(customer=request.user)
    if request.method == "POST":
        updated_form = CustomerUpdateModel(request.POST, instance=request.user)
        if updated_form.is_valid():
            updated_form.save()
            return redirect("account")
    else:
        updated_form = CustomerUpdateModel(instance=request.user)

    return render(request, "KRRR/account.html", {'updated_form':updated_form, 'orders': orders})


# admin
def adminAdmin(request):
    return render(request, 'KRRR/admin-admin.html', {})

def adminUsers(request):
    return render(request, 'KRRR/admin-users.html', { "users": User.objects.all() })


# credits
def credits(request):
    context = {}
    return render(request, 'KRRR/credits.html', context)
