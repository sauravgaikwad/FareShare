# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-14 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerride', '0004_auto_20190312_0524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='driver',
        ),
        migrations.AddField(
            model_name='ride',
            name='driverid',
            field=models.CharField(default=b'rnk', max_length=250),
        ),
    ]
