# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-13 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0007_auto_20161113_0439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='id',
        ),
        migrations.AlterField(
            model_name='content',
            name='ref_id',
            field=models.CharField(default='1', max_length=120, primary_key=True, serialize=False, unique=True),
        ),
    ]
