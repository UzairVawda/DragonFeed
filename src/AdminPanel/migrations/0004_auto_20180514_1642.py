# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-14 16:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0003_auto_20180514_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='EndDate',
            new_name='End',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='EndTime',
            new_name='Start',
        ),
        migrations.RemoveField(
            model_name='article',
            name='StartDate',
        ),
        migrations.RemoveField(
            model_name='article',
            name='StartTime',
        ),
    ]
