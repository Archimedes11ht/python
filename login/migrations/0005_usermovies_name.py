# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-12-14 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_usermovies'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermovies',
            name='name',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
    ]