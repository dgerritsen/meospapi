# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='initials',
            field=models.CharField(default='D', max_length=50),
            preserve_default=False,
        ),
    ]
