from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image_url = models.CharField(max_length=2058)
    stock = models.IntegerField()
    description = models.CharField(max_length=2058, default='No Description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


