# Generated by Django 4.1.1 on 2022-09-17 05:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0010_games_timeofpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='teamOne',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='games',
            name='teamTwo',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='games',
            name='timeofpost',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 5, 30, 43, 641019)),
        ),
    ]
