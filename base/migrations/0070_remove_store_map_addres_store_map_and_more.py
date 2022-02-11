# Generated by Django 4.0.1 on 2022-02-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0069_alter_store_map_addres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='map_addres',
        ),
        migrations.AddField(
            model_name='store',
            name='map',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(blank=True, to='base.OrderItem'),
        ),
    ]