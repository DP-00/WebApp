from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('admin-admin/', views.adminAdmin, name="admin-admin"),
    path('admin-users/', views.adminUsers, name="admin-users"),
]