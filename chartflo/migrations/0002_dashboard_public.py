# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-02 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartflo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='public',
            field=models.BooleanField(default=False, verbose_name='Public'),
        ),
    ]
