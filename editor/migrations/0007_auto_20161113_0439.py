# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-13 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0006_content_ref_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='ref_id',
            field=models.CharField(default='1', max_length=120, unique=True),
        ),
    ]
