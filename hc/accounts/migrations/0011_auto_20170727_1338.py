# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-27 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20170725_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='report_period',
            field=models.IntegerField(choices=[(1, b'daily'), (7, b'weekly'), (30, b'monthly')], default=30, null=30),
        ),
    ]