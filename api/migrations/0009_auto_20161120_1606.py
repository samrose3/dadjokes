# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-20 16:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20161113_1231'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Joke',
            new_name='Jokes',
        ),
    ]
