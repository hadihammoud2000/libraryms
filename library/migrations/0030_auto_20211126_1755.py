# Generated by Django 3.2.9 on 2021-11-26 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0029_alter_borrower_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 17, 55, 5, 111029)),
        ),
    ]
