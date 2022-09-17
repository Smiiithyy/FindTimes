# Generated by Django 4.1.1 on 2022-09-15 04:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0005_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='', max_length=255, verbose_name='image'),
        ),
    ]