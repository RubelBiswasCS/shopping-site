# Generated by Django 3.2.5 on 2021-11-08 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_productimages_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
