# Generated by Django 3.2.7 on 2021-10-23 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller_api', '0003_auto_20211023_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsize_and_quantity',
            name='product',
        ),
    ]
