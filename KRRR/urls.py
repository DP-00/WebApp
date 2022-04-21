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



    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('customer/<int:pk>/', views.UserProfileView.as_view(), name='customer'),
    path('customer/<int:pk>/delete/', views.UserDeleteView.as_view(), name='customer-delete'),
    path('login/', auth_views.LoginView.as_view(template_name="KRRR/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="KRRR/logout.html"), name='logout'),



    path('admin-admin/', views.adminAdmin, name="admin-admin"),

    path('admin-users/', views.AdminUserListView.as_view(), name="admin-users"),
    path('admin-users/<int:pk>/', views.AdminUserView.as_view(), name='admin-user'),
    path('admin-users/<int:pk>/delete/', views.AdminUserDeleteView.as_view(), name='user-delete'),
    path('admin-users/<str:username>/orders/', views.AdminUserOrderListView.as_view(), name='admin-user-orders'),
    path('admin-users/<str:username>/comments/', views.AdminUserCommentListView.as_view(), name='admin-user-comments'),

    path('admin-products/', views.AdminProductListView.as_view(), name="admin-products"),
    path('admin-products/create/', views.AdminProductCreatetView.as_view(), name="product-create"),
    path('admin-products/<int:pk>/', views.AdminProductView.as_view(), name='admin-product'),
    path('admin-products/<int:pk>/delete/', views.AdminProductDeleteView.as_view(), name='product-delete'),

    path('admin-orders/', views.AdminOrderListView.as_view(), name="admin-orders"),
    path('admin-orders/<int:pk>/', views.AdminOrderView.as_view(), name='admin-order'),
    path('admin-orders/<int:pk>/delete/', views.AdminOrderDeleteView.as_view(), name='order-delete'),

    path('admin-comments/', views.AdminCommentListView.as_view(), name="admin-comments"),
    path('admin-comments/<int:pk>/', views.AdminCommentView.as_view(), name='admin-comment'),
    path('admin-comments/<int:pk>/delete/', views.AdminCommentDeleteView.as_view(), name='comment-delete'),
]