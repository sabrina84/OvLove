# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-23 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180223_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='end_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]