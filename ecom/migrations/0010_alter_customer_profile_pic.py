# Generated by Django 4.2.8 on 2024-04-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0009_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic/CustomerProfilePic/logo.jpg', null=True, upload_to='profile_pic/CustomerProfilePic/'),
        ),
    ]
