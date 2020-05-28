from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about_us/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('products/', views.product, name='product'),
    path('products/product/detail/<int:id>/', views.product_detail, name='product_detail'),
    path('products/category/<int:category_id>/', views.product_category, name='product_category'),
    path('cart_view/', views.view_cart, name='cart'),
    path('add_to_cart/', views.add_item_to_cart, name='add_to_cart'),
    path('user_account/', views.user_account, name="account"),
    path('checkout/', views.checkout, name="checkout"),
    path('process_order/', views.process_order, name="process_order")
]