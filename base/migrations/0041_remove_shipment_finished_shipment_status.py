# Generated by Django 4.0.1 on 2022-02-02 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_remove_shipment_status_shipment_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='finished',
        ),
        migrations.AddField(
            model_name='shipment',
            name='status',
            field=models.CharField(blank=True, choices=[('Processed', 'Proccesed'), ('Sent', 'Sent'), ('Delivered', 'Delivered')], default='processed', max_length=30, null=True),
        ),
    ]
