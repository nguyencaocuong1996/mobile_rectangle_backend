# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20180107_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='services',
            field=models.ManyToManyField(blank=True, null=True, related_name='hotels', to='hotel.Service'),
        ),
    ]
