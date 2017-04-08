# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 16:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_auto_20170408_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='allowed_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]