# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartflo', '0004_question_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='height',
            field=models.PositiveSmallIntegerField(blank=True, default=400, verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='question',
            name='width',
            field=models.PositiveSmallIntegerField(blank=True, default=1200, verbose_name='Width'),
        ),
    ]
