# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-12-20 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_usermovies_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesinfo',
            name='country',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='director',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='grenre',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviesinfo',
            name='year',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermovies',
            name='country',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermovies',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermovies',
            name='director',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermovies',
            name='grenre',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermovies',
            name='year',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
    ]
