# Generated by Django 3.2.5 on 2021-11-08 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_product_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_img',
        ),
    ]
