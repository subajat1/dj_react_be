# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-29 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]