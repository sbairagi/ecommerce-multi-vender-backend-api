# Generated by Django 3.2.7 on 2021-10-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth_api', '0031_auto_20211003_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(default='None'),
        ),
    ]
