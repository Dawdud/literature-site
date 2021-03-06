# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-23 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import first.models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0008_auto_20170823_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='height_field',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=first.models.upload_location),
        ),
        migrations.AlterField(
            model_name='category',
            name='width_field',
            field=models.IntegerField(),
        ),
    ]
