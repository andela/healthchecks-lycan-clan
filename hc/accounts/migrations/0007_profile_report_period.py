# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-18 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_current_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='report_period',
            field=models.IntegerField(choices=[(b'daily', 1), (b'weekly', 7), (b'monthly', 30)], null=True),
        ),
    ]