# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 20:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20171120_0152'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserScores',
            new_name='UserScore',
        ),
    ]
