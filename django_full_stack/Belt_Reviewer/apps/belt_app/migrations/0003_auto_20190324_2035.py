# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-24 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0002_auto_20190324_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.TextField(),
        ),
    ]