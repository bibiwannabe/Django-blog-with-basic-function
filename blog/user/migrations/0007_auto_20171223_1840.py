# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-23 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20171223_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='userpic',
            field=models.ImageField(default='/static/images/default.png', upload_to='user'),
        ),
    ]
