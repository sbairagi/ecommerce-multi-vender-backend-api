# Generated by Django 3.2.7 on 2021-10-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth_api', '0025_deliveryboyprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_delivery_boy',
            field=models.BooleanField(default=False),
        ),
    ]
