# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_articles', '0002_auto_20171219_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='createdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
