from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'shop', views.ShopViewSet)


urlpatterns = [
    path('', views.index, name="index"),
    path('api/', include(router.urls)),
    path('shop/', views.shop, name="shop"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('shop/<int:id>/', views.product, name='product'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),


    path('admin-admin/', views.adminAdmin, name="admin-admin"),
    path('admin-users/', views.AdminUserListView.as_view(), name="admin-users"),
    path('admin-products/', views.AdminProductListView.as_view(), name="admin-products"),
    path('admin-products/<int:pk>/', views.AdminProductView.as_view(), name='admin-product'),
    path('admin-products/<int:pk>/delete/', views.AdminProductDeleteView.as_view(), name='product-delete'),
    
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('customer/<int:pk>/', views.UserProfileView.as_view(), name='customer'),
    path('customer/<int:pk>/delete/', views.UserDeleteView.as_view(), name='customer-delete'),
    path('login/', auth_views.LoginView.as_view(template_name="KRRR/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="KRRR/logout.html"), name='logout'),
]