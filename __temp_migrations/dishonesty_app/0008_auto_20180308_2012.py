# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-09 01:12
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('dishonesty_app', '0007_auto_20180308_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='diff_guess',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='receiver_guess',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
