# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0022_rasschet_norm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rasschet',
            name='norm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Norm'),
        ),
    ]
