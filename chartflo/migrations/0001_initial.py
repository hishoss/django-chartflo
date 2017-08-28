# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('slug', models.CharField(max_length=120, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Dashboard',
                'verbose_name_plural': 'Dashboards',
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Filter',
                'verbose_name_plural': 'Filters',
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('app', models.CharField(max_length=120, verbose_name='App')),
                ('model', models.CharField(max_length=120, verbose_name='Model')),
                ('filters', models.ManyToManyField(blank=True, related_name='queries', to='chartflo.Filter', verbose_name='Filters')),
            ],
            options={
                'verbose_name': 'Query',
                'verbose_name_plural': 'Queries',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('html', models.TextField(blank=True, verbose_name='Html')),
                ('script', models.TextField(blank=True, verbose_name='Script')),
                ('queries', models.ManyToManyField(related_name='questions', to='chartflo.Query', verbose_name='Queries')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.AddField(
            model_name='dashboard',
            name='questions',
            field=models.ManyToManyField(related_name='dashboards', to='chartflo.Question', verbose_name='Questions'),
        ),
    ]
