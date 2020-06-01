from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description', 'category_id')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'transaction_id', 'completed', 'date_ordered')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderProduct)
admin.site.register(ShippingAddress)
admin.site.register(Order, OrderAdmin)
