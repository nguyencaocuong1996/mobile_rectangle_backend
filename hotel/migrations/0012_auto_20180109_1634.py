# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 16:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_auto_20180109_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedhotel',
            name='bookedAt',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='bookedhotel',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
