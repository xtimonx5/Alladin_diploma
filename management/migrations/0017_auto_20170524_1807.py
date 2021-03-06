# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_auto_20170524_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='bev',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='БЭВ'),
        ),
        migrations.AddField(
            model_name='food',
            name='calorie_o',
            field=models.FloatField(blank=True, null=True, verbose_name='Обмен энергией O'),
        ),
        migrations.AddField(
            model_name='food',
            name='calorie_с',
            field=models.FloatField(blank=True, null=True, verbose_name='Обмен энергией С'),
        ),
        migrations.AddField(
            model_name='food',
            name='hlor',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Хлор'),
        ),
        migrations.AddField(
            model_name='food',
            name='lizin',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Лизин'),
        ),
        migrations.AddField(
            model_name='food',
            name='mecionin_cistin',
            field=models.FloatField(default=0, null=True, verbose_name='Метионин + Цистин'),
        ),
        migrations.AlterField(
            model_name='food',
            name='calorie',
            field=models.FloatField(blank=True, null=True, verbose_name='Обмен энергией КРС'),
        ),
    ]
