# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-05 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='packagingType',
            new_name='type_packaging',
        ),
    ]