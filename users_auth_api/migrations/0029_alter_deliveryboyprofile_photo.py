# Generated by Django 3.2.7 on 2021-10-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth_api', '0028_remove_deliveryboyprofile_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryboyprofile',
            name='photo',
            field=models.ImageField(upload_to='delivery_boy_photos'),
        ),
    ]
