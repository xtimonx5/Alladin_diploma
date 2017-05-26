from django.db import models
from .animal_type import AnimalType
from .farm import Farm
from .farm_group import FarmGroup

from smart_selects.db_fields import ChainedForeignKey


class Animal(models.Model):
    type = models.ForeignKey(AnimalType)
    name = models.CharField(max_length=50)
    farm = models.ForeignKey(Farm, blank=True)
    date_of_birth = models.DateField()
    date_of_last_sex = models.DateField( null=True,blank=True)
    current_weight = models.IntegerField()
    group = ChainedForeignKey(FarmGroup, chained_field='farm', chained_model_field='farm',show_all=False, auto_choose=True, sort=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.farm = self.group.farm
        return super(Animal, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.type.name + ' ' + str(self.id)
