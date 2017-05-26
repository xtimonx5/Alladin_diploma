from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from .farm import Farm
from .farm_group import FarmGroup
from smart_selects.db_fields import ChainedManyToManyField
from .food import Food
from .norm import Norm
from .animal_type import AnimalType

class Rasschet(models.Model):
    # date =
    farm = models.ForeignKey(Farm)
    group = ChainedForeignKey(FarmGroup, chained_field='farm', chained_model_field='farm', show_all=False,
                              auto_choose=True, sort=True)
    type = models.ForeignKey(AnimalType, null=True, blank=True)
    norm = ChainedForeignKey(Norm, chained_field='type',chained_model_field='animal_type', auto_choose=True, sort=True)