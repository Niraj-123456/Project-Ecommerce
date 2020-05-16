from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='forms/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('products/', views.product, name='product'),
    path('products/product/detail/<int:id>/', views.product_detail, name='product_detail'),
    path('products/category/<int:category_id>/', views.product_category, name='product_category')
]