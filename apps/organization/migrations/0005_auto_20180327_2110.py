# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-27 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20180326_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='fav_nums',
            field=models.IntegerField(default=0, verbose_name='收藏数'),
        ),
    ]
