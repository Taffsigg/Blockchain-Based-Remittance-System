# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 18:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='list_id',
        ),
    ]
