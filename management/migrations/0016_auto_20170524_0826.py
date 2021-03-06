# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_auto_20170524_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='cost',
        ),
        migrations.AddField(
            model_name='food',
            name='Perev_proteine',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Переваренный протеин'),
        ),
        migrations.AddField(
            model_name='food',
            name='Siro_proteine',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сырой протеин'),
        ),
        migrations.AddField(
            model_name='food',
            name='natri',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Натрий'),
        ),
        migrations.AddField(
            model_name='food',
            name='sir_cletchatka',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сыр клетчатка'),
        ),
        migrations.AddField(
            model_name='food',
            name='sir_jir',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сыр жир'),
        ),
        migrations.AddField(
            model_name='food',
            name='sol',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Соль'),
        ),
        migrations.AddField(
            model_name='food',
            name='suh_veschestvo',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сухое вещество'),
        ),
        migrations.AddField(
            model_name='food',
            name='сorm',
            field=models.FloatField(default=1, verbose_name='Корм'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='norm',
            name='сorm',
            field=models.FloatField(default=1, verbose_name='Корм'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='calcii',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Кальций'),
        ),
        migrations.AlterField(
            model_name='food',
            name='cali',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Калий'),
        ),
        migrations.AlterField(
            model_name='food',
            name='calorie',
            field=models.FloatField(verbose_name='Обмен энергией'),
        ),
        migrations.AlterField(
            model_name='food',
            name='cink',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Цинк'),
        ),
        migrations.AlterField(
            model_name='food',
            name='fosfor',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Фосфор'),
        ),
        migrations.AlterField(
            model_name='food',
            name='iod',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Йод'),
        ),
        migrations.AlterField(
            model_name='food',
            name='jelezo',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Железо'),
        ),
        migrations.AlterField(
            model_name='food',
            name='karotin',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Каротин'),
        ),
        migrations.AlterField(
            model_name='food',
            name='kobalt',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Кобальт '),
        ),
        migrations.AlterField(
            model_name='food',
            name='krahmal',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Крахмал'),
        ),
        migrations.AlterField(
            model_name='food',
            name='magnie',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Магний'),
        ),
        migrations.AlterField(
            model_name='food',
            name='marganec',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Марганец'),
        ),
        migrations.AlterField(
            model_name='food',
            name='med',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Медь'),
        ),
        migrations.AlterField(
            model_name='food',
            name='sera',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сера'),
        ),
        migrations.AlterField(
            model_name='food',
            name='sugar',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сахар'),
        ),
        migrations.AlterField(
            model_name='food',
            name='vit_a',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Витамин А'),
        ),
        migrations.AlterField(
            model_name='food',
            name='vit_d',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Витамин Д'),
        ),
        migrations.AlterField(
            model_name='food',
            name='vit_e',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Витамин Е'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='Siro_proteine',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сырой протеин'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='calcii',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Кальций'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='cali',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Калий'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='cink',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Цинк'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='fosfor',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Фосфор'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='iod',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Йод'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='jelezo',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Железо'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='karotin',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Каротин'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='kobalt',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Кобальт '),
        ),
        migrations.AlterField(
            model_name='norm',
            name='krahmal',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Крахмал'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='magnie',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Магний'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='marganec',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Марганец'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='med',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Медь'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='natri',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Натрий'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='sera',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сера'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='sir_jir',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сыр жир'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='sugar',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сахар'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='suh_veschestvo',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Сухое вещество'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='vit_a',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Витамин А'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='vit_d',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Витамин Д'),
        ),
        migrations.AlterField(
            model_name='norm',
            name='vit_e',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Витамин Е'),
        ),
    ]
