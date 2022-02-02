# Generated by Django 4.0.1 on 2022-02-02 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='finished',
        ),
        migrations.AddField(
            model_name='shipment',
            name='status',
            field=models.CharField(choices=[('processed', 'Proccesed'), ('sent', 'Sent'), ('delvered', 'Delivered')], default='processed', max_length=30),
        ),
    ]
