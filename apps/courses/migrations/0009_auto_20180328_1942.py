# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-28 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_lesson_learn_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='learn_time',
        ),
        migrations.AddField(
            model_name='video',
            name='learn_time',
            field=models.IntegerField(default=0, verbose_name='学习时长(分钟数)'),
        ),
    ]
