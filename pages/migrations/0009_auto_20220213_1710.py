# Generated by Django 3.1.4 on 2022-02-13 17:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20220213_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 17, 10, 51, 352434, tzinfo=utc)),
        ),
    ]
