# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0008_personsignal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dangers',
            field=models.ManyToManyField(blank=True, null=True, to='persons.DangerClass'),
        ),
    ]
