# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-09 00:59
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('dishonesty_app', '0005_auto_20180308_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='dump_guess_answer',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]