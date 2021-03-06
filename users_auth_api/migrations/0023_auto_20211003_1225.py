# Generated by Django 3.2.7 on 2021-10-03 12:25

from django.db import migrations, models
import django.db.models.deletion
import users_auth_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth_api', '0022_auto_20211003_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalerDetail',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users_auth_api.user')),
                ('is_sales', models.BooleanField(default=True)),
                ('photo', models.ImageField(default='default.png', upload_to=users_auth_api.models.get_image_path)),
                ('adharcard', models.ImageField(default='default.png', upload_to=users_auth_api.models.get_image_path)),
                ('pancard', models.ImageField(default='default.png', upload_to=users_auth_api.models.get_image_path)),
                ('gumasta', models.ImageField(default='default.png', upload_to=users_auth_api.models.get_image_path)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('gst_Number', models.CharField(max_length=15, null=True)),
                ('shop_Name', models.CharField(max_length=500, null=True)),
                ('whatsapp_no', models.CharField(max_length=10, null=True)),
                ('shop_Address', models.TextField()),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('landmark', models.CharField(max_length=500, null=True)),
                ('locality', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], max_length=50, null=True)),
                ('account_Holder_Name', models.CharField(max_length=50, null=True)),
                ('account_Number', models.CharField(max_length=20, null=True)),
                ('ifsc_Code', models.CharField(max_length=11, null=True)),
                ('bank_name', models.CharField(max_length=20, null=True)),
                ('aproved_user', models.CharField(default='False', max_length=6)),
                ('product_limite', models.CharField(default='25', max_length=3)),
                ('seller_join_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_user',
            field=models.BooleanField(default=True),
        ),
    ]
