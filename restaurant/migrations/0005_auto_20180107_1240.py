# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-07 12:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20171214_1747'),
        ('restaurant', '0004_auto_20171217_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedRestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('bookedAt', models.DateField(blank=True, default=datetime.datetime.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_restaurant_meta', to='customer.Customer')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_customer_meta', to='restaurant.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteRestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_restaurant_meta', to='customer.Customer')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_customer_meta', to='restaurant.Restaurant')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='favoriterestaurant',
            unique_together=set([('customer', 'restaurant')]),
        ),
    ]
