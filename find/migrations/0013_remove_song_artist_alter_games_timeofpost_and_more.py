# Generated by Django 4.1.1 on 2022-09-17 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0012_alter_games_timeofpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AlterField(
            model_name='games',
            name='timeofpost',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 6, 12, 31, 372640)),
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
