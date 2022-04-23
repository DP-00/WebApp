from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

import requests
from rest_framework import viewsets
from .serializers import ProductSerializer

from django.db.models import Sum, Min


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
def add_comment(request, id):
    product = Product.objects.get(id=id)
    form = UserCommentForm()
    if request.method == "POST":
        form  = UserCommentForm(request.POST)
        if form.is_valid():
            content = form.data['content']
            c = Comment(product=product, customer=request.user, content=content, stars=form.data['stars'], comment_date=datetime.now())
            c.save()
            return redirect('product', id)

    context = {
        'form': form
    }

    return render(request, 'KRRR/add-comment.html', context)


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
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserRegistrationForm()
    return render(request, "KRRR/register.html", {'form':form})


@login_required
def account(request):
    orders = Order.objects.filter(customer=request.user)
    if request.method == "POST":
        updated_form = UserUpdateForm(request.POST, instance=request.user)
        if updated_form.is_valid():
            updated_form.save()
            return redirect("account")
    else:
        updated_form = UserUpdateForm(instance=request.user)

    return render(request, "KRRR/account.html", {'updated_form':updated_form, 'orders': orders})



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


# credits
def credits(request):
    context = {}
    return render(request, 'KRRR/credits.html', context)
