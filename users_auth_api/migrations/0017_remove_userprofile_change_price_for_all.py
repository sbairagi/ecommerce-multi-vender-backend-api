# Generated by Django 2.1.9 on 2020-05-28 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth_api', '0016_auto_20200528_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='change_price_for_all',
        ),
    ]
