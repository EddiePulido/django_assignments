# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-25 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0003_auto_20190324_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=1),
        ),
    ]
