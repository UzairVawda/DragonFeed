# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 06:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Orginization', models.CharField(blank=True, max_length=50)),
                ('Location', models.CharField(max_length=100)),
                ('Description', models.TextField(blank=True)),
                ('Start', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('End', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Link', models.CharField(blank=True, max_length=500)),
                ('Tag', models.CharField(max_length=20)),
                ('Flyer', models.FileField(upload_to=b'')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]