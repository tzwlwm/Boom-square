# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-02-12 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='app_blog',
            options={'ordering': ['-time_now']},
        ),
    ]