# Generated by Django 4.0.1 on 2022-02-10 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0063_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]
