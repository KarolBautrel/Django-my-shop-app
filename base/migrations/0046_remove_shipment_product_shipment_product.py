# Generated by Django 4.0.1 on 2022-02-08 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0045_remove_cart_owner_user_cart_alter_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='product',
        ),
        migrations.AddField(
            model_name='shipment',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='base.Product'),
        ),
    ]