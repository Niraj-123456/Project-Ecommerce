from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image_url = models.CharField(max_length=2058)
    stock = models.IntegerField()
    description = models.CharField(max_length=2058, default='No Description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    completed = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def get_cart_total(self):
        orderproducts = self.orderproduct_set.all()
        total = sum([product.get_total for product in orderproducts])
        return total

    @property
    def get_cart_items(self):
        orderproducts = self.orderproduct_set.all()
        total = sum([product.quantity for product in orderproducts])
        return total


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.product.name)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255)
    town_city = models.CharField(max_length=255)
    phone = models.IntegerField(null=False, blank=False)
    email = models.CharField(max_length=255)
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Shipping Addresses'

    def __str__(self):
        return self.street








