# Generated by Django 4.2.8 on 2024-04-05 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_alter_customer_address_alter_customer_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(default='profile_pic/CustomerProfilePic/logo.jpg', null=True, upload_to='profile_pic/CustomerProfilePic/'),
        ),
    ]
