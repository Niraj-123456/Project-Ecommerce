# Generated by Django 3.0.1 on 2020-05-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='size',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
