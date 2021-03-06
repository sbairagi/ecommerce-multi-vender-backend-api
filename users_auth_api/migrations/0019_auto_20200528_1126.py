# Generated by Django 2.1.9 on 2020-05-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth_api', '0018_apppricing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apppricing',
            options={'verbose_name': 'App Pricing & Trial Period', 'verbose_name_plural': 'App Pricing  & Trial Period'},
        ),
        migrations.AddField(
            model_name='apppricing',
            name='trial_period_days',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='apppricing',
            name='in_app_pricing',
            field=models.IntegerField(default=5320),
        ),
    ]
