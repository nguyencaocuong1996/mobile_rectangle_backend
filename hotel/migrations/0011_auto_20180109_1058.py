# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_auto_20180109_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(blank=True, default='image/hotel/default.jpg', null=True, upload_to='image/hotel'),
        ),
    ]