from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'shop', views.ShopViewSet)

urlpatterns = [
    path('', views.index, name="index"),

# API urls
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

# shopping urls
    path('shop/', views.shop, name="shop"),
    path('shop/<int:id>/', views.product, name='product'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

# customer urls
    path('register/', views.register, name='register'),
    path('customer/', views.customer, name='customer'),
    path('login/', auth_views.LoginView.as_view(template_name="KRRR/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="KRRR/logout.html"), name='logout'),

# admin urls
    path('admin-admin/', views.adminAdmin, name="admin-admin"),
    path('admin-users/', views.adminUsers, name="admin-users"),

# credits
    path('credits/', views.credits, name="credits"),
]