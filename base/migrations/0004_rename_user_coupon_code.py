# Generated by Django 4.0.1 on 2022-02-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_order_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='user',
            new_name='code',
        ),
    ]
