# Generated by Django 3.0.1 on 2021-11-14 23:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20211114_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 15, 23, 35, 7, 707291)),
        ),
    ]
