# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='store_image',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
