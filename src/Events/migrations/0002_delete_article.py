# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]
