# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-23 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.BooleanField(default=False),
        ),
    ]