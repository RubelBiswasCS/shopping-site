# Generated by Django 3.2.5 on 2021-11-08 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210910_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(blank=True, default='no-product-image.png', null=True, upload_to='images/'),
        ),
    ]
