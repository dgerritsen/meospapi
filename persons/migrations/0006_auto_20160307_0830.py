# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-07 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_auto_20160306_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=5)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='birth_country',
            field=models.CharField(default='Nederland', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('u', 'Unknown')], default='m', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='nationality',
            field=models.CharField(default='Nederlandse', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='persons.Person'),
        ),
    ]