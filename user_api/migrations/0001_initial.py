# Generated by Django 3.2.7 on 2021-10-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BottomUserSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('image', models.ImageField(upload_to='seller_slider_img')),
                ('category', models.CharField(default='#', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CenterUserSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('image', models.ImageField(upload_to='seller_slider_img')),
                ('category', models.CharField(default='#', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopUserSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('image', models.ImageField(upload_to='seller_slider_img')),
                ('category', models.CharField(default='#', max_length=50, null=True)),
            ],
        ),
    ]
