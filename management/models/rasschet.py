from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from .farm import Farm
from .farm_group import FarmGroup
from smart_selects.db_fields import ChainedManyToManyField
from .food import Food
from .norm import Norm
from .animal_type import AnimalType

class Rasschet(models.Model):
    MONTH_CHOICES = (
        ('Январь','Январь'),
        ('Февраль', 'Февраль'),
        ('Март', 'Март'),
        ('Апрель', 'Апрель'),
        ('Май', 'Май'),
        ('Июнь', 'Июнь'),
        ('Июль', 'Июль'),
        ('Август', 'Август'),
        ('Сентябрь', 'Сентябрь'),
        ('Октябрь', 'Октябрь'),
        ('Ноябрь', 'Ноябрь'),
        ('Декабрь', 'Декабрь'),

    )

    month=models.CharField(max_length=30, choices=MONTH_CHOICES, null=True,blank=True, verbose_name='Месяц')
    year = models.IntegerField(null=True,blank=True, verbose_name='Год')
    farm = models.ForeignKey(Farm, verbose_name='Ферма')
    group = ChainedForeignKey(FarmGroup, chained_field='farm', chained_model_field='farm', show_all=False,
                              auto_choose=True, sort=True,)
    type = models.ForeignKey(AnimalType, null=True, blank=True, verbose_name='Тип животных')
    norm = ChainedForeignKey(Norm, chained_field='type',chained_model_field='animal_type', auto_choose=True, sort=True)

    def __str__(self):
        return str(self.year) + ' ' + str(self.month) + ' ' + self.farm.name + ' ' +self.group.name

    class Meta:
        verbose_name = 'Рассчет'
        verbose_name_plural = 'Рассчеты'