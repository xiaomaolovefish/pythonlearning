# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 16:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShareHouse', '0002_remove_shareh_submit_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shareh',
            name='InputFile',
        ),
    ]
