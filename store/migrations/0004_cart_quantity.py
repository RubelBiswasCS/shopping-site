# Generated by Django 3.2.5 on 2021-07-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210728_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
