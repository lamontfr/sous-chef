# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-18 03:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0014_auto_20160513_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='street number'),
    )]