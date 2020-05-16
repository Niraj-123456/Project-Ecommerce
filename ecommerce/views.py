from django.shortcuts import render
from .models import Product, Category
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserFrom


def index(request):
    return render(request, 'index.html')


def product(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products.html', {'products': products, 'categories': categories})


def product_detail(request, id):
    products = Product.objects.filter(id=id)
    return render(request, 'product_detail.html', {'products': products})


def product_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'products.html', {'products': products, 'categories': categories})


def register(request):
    form = CreateUserFrom()
    if request.method == 'POST':
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'forms/register.html', context)

