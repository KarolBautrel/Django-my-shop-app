# Generated by Django 4.0.1 on 2022-02-10 22:31

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0062_alter_product_image_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=django_resized.forms.ResizedImageField(crop=['top', 'left'], default='avatar.svg', force_format=None, keep_meta=True, null=True, quality=0, size=[100, 100], upload_to='whatever'),
        ),
    ]