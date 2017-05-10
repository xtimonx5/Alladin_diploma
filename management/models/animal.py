from django.db import models
from .animal_type import AnimalType
from .farm import Farm


class Animal(models.Model):
    type = models.ForeignKey(AnimalType)
    name = models.CharField(max_length=50)
    farm = models.ForeignKey(Farm)
    date_of_birth = models.DateField()
    date_of_last_sex = models.DateField()
    current_weight = models.IntegerField()

    def __str__(self):
        return self.type.name + ' ' + str(self.id)
