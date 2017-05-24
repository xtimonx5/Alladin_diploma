# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_auto_20170524_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='norm',
            name='natri',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='Perev_proteine',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Переваренный протеин'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='Siro_proteine',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='calcii',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='cali',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='calorie',
            field=models.FloatField(verbose_name='Обмен энергией'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='cink',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='fosfor',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='iod',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='jelezo',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='karotin',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='kobalt',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='krahmal',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='magnie',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='marganec',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='med',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='sera',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='sir_cletchatka',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сыр клетчатка'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='sir_jir',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='sol',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Соль'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='sugar',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='suh_veschestvo',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='vit_a',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='vit_d',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='norm',
            name='vit_e',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
