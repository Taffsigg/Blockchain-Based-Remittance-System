# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0015_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='amount',
            field=models.CharField(default=1, max_length=40),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='recipient',
            field=models.CharField(default=1, max_length=300),
        ),
    ]
