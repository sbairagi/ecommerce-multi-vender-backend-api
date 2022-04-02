# Generated by Django 3.2.7 on 2021-10-04 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth_api', '0037_auto_20211004_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryboyprofile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sallerdetail',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='deliveryboyprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='deliveryboyprofile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sallerdetail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='sellerprofile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='userprofile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
