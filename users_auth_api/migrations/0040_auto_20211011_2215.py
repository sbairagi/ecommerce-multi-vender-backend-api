# Generated by Django 3.2.7 on 2021-10-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth_api', '0039_alter_sallerdetail_aproved_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sallerdetail',
            name='aproved_user',
        ),
        migrations.AddField(
            model_name='user',
            name='aproved_seller',
            field=models.BooleanField(default=False, max_length=6),
        ),
    ]
