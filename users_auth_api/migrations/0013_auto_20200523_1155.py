# Generated by Django 2.1.9 on 2020-05-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth_api', '0012_userprofile_in_app_price_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='in_app_price_display',
            field=models.IntegerField(default=1999, help_text='Please put only digits', max_length=5),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='trial_period_days',
            field=models.IntegerField(default=30, max_length=5),
        ),
    ]
