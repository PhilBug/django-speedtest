# Generated by Django 3.1.5 on 2021-01-28 23:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0003_auto_20210128_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='test_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
