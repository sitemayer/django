# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-10 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=20)),
            ],
        ),
    ]
