# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-16 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('rollno', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
