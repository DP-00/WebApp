from distutils.errors import CompileError
from pyexpat import model
from turtle import mode
from attr import fields
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from yaml import serialize_all
from .models import *
from .forms import *
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
    success_url = reverse_lazy('login')
    template_name = 'KRRR/register.html'

class UserProfileView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'KRRR/customer.html'
    success_url = '/'

class UserDeleteView(DeleteView):
    model = User
    template_name = 'KRRR/customer-delete.html'
    success_url = '/'

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False
    


##########   ADMIN VIEWS   ##########
def adminAdmin(request):
    return render(request, 'KRRR/admin-admin.html', {})


            ### USERS ###
class AdminUserListView(ListView):
    model = User
    template_name = 'KRRR/admin-users.html'
    context_object_name = 'users'
    paginate_by = 7

class AdminUserView(DetailView):
    model = User
    template_name = 'KRRR/admin-user.html'

class AdminUserDeleteView(DeleteView):
    model = User
    template_name = 'KRRR/user-delete.html'
    success_url = reverse_lazy('admin-users')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


            ### PRODUCTS ###
class AdminProductCreatetView(CreateView):
    form_class = ProductForm
    success_url = reverse_lazy('admin-products')
    template_name = 'KRRR/product-create.html'

class AdminProductListView(ListView):
    model = Product
    template_name = 'KRRR/admin-products.html'
    context_object_name = 'products'
    paginate_by = 7

class AdminProductView(UpdateView):
    model = Product
    success_url = reverse_lazy('admin-products')
    form_class = ProductForm
    template_name = 'KRRR/admin-product.html'
    context_object_name = 'product'

class AdminProductDeleteView(DeleteView):
    model = Product
    template_name = 'KRRR/product-delete.html'
    success_url = reverse_lazy('admin-products')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


            ### ORDERS ###
class AdminOrderListView(ListView):
    model = Order
    template_name = 'KRRR/admin-orders.html'
    context_object_name = 'orders'
    paginate_by = 7

class AdminOrderView(UpdateView):
    model = Order
    success_url = reverse_lazy('admin-orders')
    form_class = OrderForm
    template_name = 'KRRR/admin-order.html'
    context_object_name = 'order'

class AdminOrderDeleteView(DeleteView):
    model = Order
    template_name = 'KRRR/order-delete.html'
    success_url = reverse_lazy('admin-orders')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class AdminUserOrderListView(ListView):
    model = Order
    template_name = 'KRRR/admin-user-orders.html'
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Order.objects.filter(customer=user).order_by('-order_date')



            ### COMMENTS ###
class AdminCommentListView(ListView):
    model = Comment
    template_name = 'KRRR/admin-comments.html'
    context_object_name = 'comments'
    paginate_by = 7

class AdminCommentView(DetailView):
    model = Comment
    template_name = 'KRRR/admin-comment.html'
    context_object_name = 'comment'

class AdminCommentDeleteView(DeleteView):
    model = Comment
    template_name = 'KRRR/comment-delete.html'
    success_url = reverse_lazy('admin-comments')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class AdminUserCommentListView(ListView):
    model = Comment
    template_name = 'KRRR/admin-user-comments.html'
    context_object_name = 'comments'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Comment.objects.filter(customer=user).order_by('-comment_date')