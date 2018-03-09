# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-08 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0007_transportwithordertransection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expire_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='export_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturing_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
