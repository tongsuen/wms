# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-06 07:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('program', '0003_product_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecieveProductAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=255)),
                ('product_detail', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=120, null=True)),
                ('tel', models.CharField(max_length=120, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
