# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-21 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20161213_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='kind',
            field=models.CharField(choices=[(b'email', b'Email'), (b'webhook', b'Webhook'), (b'hipchat', b'HipChat'), (b'slack', b'Slack'), (b'pd', b'PagerDuty'), (b'po', b'Pushover'), (b'pushbullet', b'Pushbullet'), (b'opsgenie', b'OpsGenie'), (b'victorops', b'VictorOps'), (b'discord', b'Discord')], max_length=20),
        ),
    ]
