# Generated by Django 3.2.5 on 2021-08-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_order_temp_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
