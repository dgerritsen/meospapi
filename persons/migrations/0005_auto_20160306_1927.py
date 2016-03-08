# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_auto_20160306_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dangerclass',
            name='danger',
        ),
        migrations.AddField(
            model_name='dangerclass',
            name='code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dangerclass',
            name='description',
            field=models.CharField(default='Desc', max_length=200),
            preserve_default=False,
        ),
    ]