# Generated by Django 4.0.1 on 2022-01-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_user_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
