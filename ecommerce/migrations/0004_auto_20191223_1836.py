# Generated by Django 3.0.1 on 2019-12-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='No Description', max_length=2058),
        ),
    ]