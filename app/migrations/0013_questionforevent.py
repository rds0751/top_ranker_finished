# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 20:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_auto_20171120_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionForEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(choices=[('e', 'easy'), ('m', 'medium'), ('h', 'hard')], default='e', max_length=10)),
                ('desc', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Event')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]