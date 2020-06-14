from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description', 'date_added', 'category_id', 'discount_id')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_id', 'completed', 'date_ordered')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderProduct)
admin.site.register(ShippingAddress)
admin.site.register(Order, OrderAdmin)
admin.site.register(Discount)
