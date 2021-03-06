# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='qualification',
            field=models.CharField(choices=[('ug', 'UnderGraduate'), ('pg', 'PostGraduate'), ('phd', 'PHD'), ('fac', 'faculty'), ('ind', 'industrial'), ('No', 'None')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='university',
            field=models.CharField(default='', max_length=100),
        ),
    ]
