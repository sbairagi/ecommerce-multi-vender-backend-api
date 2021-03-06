# Generated by Django 2.1.9 on 2020-04-20 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notificationsapi', '0005_auto_20200414_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericnotification',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who_created_generic_notification', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='genericnotification',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who_updated_generic_notification', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stocktip',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stocktip',
            name='updated_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='genericnotification',
            name='notification_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stocktip',
            name='stock_tip_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
