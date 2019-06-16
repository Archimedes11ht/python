# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-12-12 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20181207_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('span', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('actors', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='confirmstring',
            options={},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
    ]
