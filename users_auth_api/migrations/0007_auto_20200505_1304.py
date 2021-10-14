# Generated by Django 2.1.9 on 2020-05-05 13:04

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth_api', '0006_auto_20200505_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='permissions',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Short Term', 'Short Term'), ('Long Term', 'Long Term'), ('Intraday', 'Intraday'), ('Commodity', 'Commodity')], default=('ST', 'LT', 'ID', 'CD'), max_length=20),
        ),
    ]
