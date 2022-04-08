from django.shortcuts import redirect, render
from .models import *
from .forms import CustomerRegistrationModel, CustomerUpdateModel
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def index(request):
    context = {}
    return render(request, 'KRRR/index.html', context)


def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'KRRR/shop.html', context)

def product(request, id):
    product = Product.objects.get(id = id)
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
    return render(request, 'KRRR/admin-users.html', { "users": Customer.objects.all() })