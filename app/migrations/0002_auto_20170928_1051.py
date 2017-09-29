# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
