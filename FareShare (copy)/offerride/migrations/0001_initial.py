# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-12 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charno', models.IntegerField()),
                ('color', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('psw', models.CharField(max_length=240)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offerride.Driver'),
        ),
    ]
