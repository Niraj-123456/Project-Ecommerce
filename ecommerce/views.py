from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
import datetime
from django.contrib import messages
from .forms import CreateUserFrom
from django.core.paginator import Paginator
from .utils import *


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def product(request):
    products = Product.objects.filter().order_by('-date_added')
    categories = Category.objects.all()
    paginator = Paginator(products, per_page=8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj.object_list,
               'categories': categories,
               'paginator': paginator,
               'page_number': int(page_number)
               }
    return render(request, 'products.html', context)


def product_detail(request, id):
    products = Product.objects.filter(id=id)
    return render(request, 'product_detail.html', {'products': products})


def product_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    paginator = Paginator(products, per_page=8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj.object_list,
               'categories': categories,
               'paginator': paginator,
               'page_number': int(page_number)
               }
    return render(request, 'products.html', context)


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your account has been created successfully! please, Login to access your account')
            return redirect('login')
    else:
        form = CreateUserFrom()
    return render(request, 'forms/register.html', {'form': form})


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product')
        else:
            messages.info(request, 'email or password incorrect')
    return render(request, 'forms/login.html')


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def user_account(request):
    return render(request, 'useraccount.html')


@login_required(login_url='login')
def add_item_to_cart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=user, completed=False)
    orderProduct, created = OrderProduct.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderProduct.quantity += 1
        messages.success(request, 'Product added to your cart successfully')

    elif action == 'remove':
        orderProduct.quantity -= 1
        messages.warning(request, 'Quantity updated successfully')

    elif action == 'delete':
        orderProduct.quantity = 0
        messages.warning(request, 'Product successfully removed from your cart.')

    orderProduct.save()

    if orderProduct.quantity <= 0:
        orderProduct.delete()

    return JsonResponse("Product updated successfully", safe=False)


# @login_required(login_url='login')
# def add_item_to_cart(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#
#     print(productId)
#     print(action)
#
#     user = request.user
#
#     product = Product.objects.get(id=productId)
#
#     order, created = Order.objects.get_or_create(user=user, completed=False)
#
#     orderProduct, created = OrderProduct.objects.get_or_create(order=order, product=product)
#
#     if action == 'add':
#         orderProduct.quantity = (orderProduct.quantity + 1)
#         messages.success(request, 'Product added to your cart successfully.')
#
#     elif action == 'remove':
#         orderProduct.quantity = (orderProduct.quantity - 1)
#         messages.info(request, 'Product updated in your cart.')
#
#     elif action == 'delete':
#         orderProduct.quantity = 0
#         messages.warning(request, 'Product has been removed from the cart successfully.')
#
#     orderProduct.save()
#
#     if orderProduct.quantity <= 0:
#         orderProduct.delete()
#
#     return JsonResponse("Product Added to cart", safe=False)

@login_required(login_url='login')
def view_cart(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, completed=False)
        products = order.orderproduct_set.all()

    context = {'products': products, 'order': order}
    return render(request, 'cart.html', context)


@login_required(login_url='login')
def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, completed=False)
        products = order.orderproduct_set.all()
    context = {'products': products, 'order': order}
    return render(request, 'checkout.html', context)


# @login_required(login_url='login')
# def process_order(request):
#     data = json.loads(request.body)
#     transaction_id = datetime.datetime.now().timestamp()
#     if request.user.is_authenticated:
#         user = request.user
#         order, created = Order.objects.get_or_create(user=user, completed=False)
#         messages.success(request, 'Your Order has been successfully created.')
# 
#     total = data['shipping-info']['total']
#     order.transaction_id = transaction_id
# 
#     if total == order.get_cart_total:
#         order.completed = True
#         print("order completed")
# 
#     order.save()
# 
#     ShippingAddress.objects.create(
#         user=user,
#         order=order,
#         firstname=data['shipping-info']['firstname'],
#         lastname=data['shipping-info']['lastname'],
#         street=data['shipping-info']['street'],
#         town_city=data['shipping-info']['towncity'],
#         phone=data['shipping-info']['phone'],
#         email=data['shipping-info']['email']
#     )
#     # else:
#         # customer, order = guest_order(request, data)
#     # total = data['shipping-info']['total']
#     # order.transaction_id = transaction_id
#     # if total == order.get_cart_total:
#     #     order.completed = True
#     #     print("order completed")
#     # order.save()
#     #
#     # ShippingAddress.objects.create(
#     #     user=user,
#     #     order=order,
#     #     firstname=data['shipping-info']['firstname'],
#     #     lastname=data['shipping-info']['lastname'],
#     #     street=data['shipping-info']['street'],
#     #     town_city=data['shipping-info']['towncity'],
#     #     phone=data['shipping-info']['phone'],
#     #     email=data['shipping-info']['email']
#     # )
# 
#     return JsonResponse("Order submitted", safe=False)

@login_required(login_url='login')
def process_order(request):
    data = json.loads(request.body)
    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, completed=False)
        total = float(data['shipping-info']['total'])
        order.transaction_id = transaction_id
        if total == float(order.get_cart_total):
            order.completed = True
            print("order completed")
            order.save()
    ShippingAddress.objects.create(
        user=user,
        order=order,
        firstname=data['shipping-info']['firstname'],
        lastname=data['shipping-info']['lastname'],
        street=data['shipping-info']['street'],
        town_city=data['shipping-info']['towncity'],
        phone=data['shipping-info']['phone'],
        email=data['shipping-info']['email']
    )
    messages.success(request, 'Your order has been successfully placed.')
    return JsonResponse("Your order has been placed successfully", safe=False)
