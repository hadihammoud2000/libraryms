# Generated by Django 3.0.1 on 2021-11-18 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_auto_20211118_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 19, 56, 6, 547982)),
        ),
        migrations.AlterUniqueTogether(
            name='borrower',
            unique_together=set(),
        ),
    ]
