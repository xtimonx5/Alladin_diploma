from django.db import models

from ..animal import Animal


class MilkYield(models.Model):
    date = models.DateField()
    weight = models.IntegerField()
    animal = models.ForeignKey(Animal, related_name='yields')

    # For monthly yield
    fat_content = models.IntegerField(null=True, blank=True)
    protein_content = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Удой молока'
        verbose_name_plural = 'Удои молока'
