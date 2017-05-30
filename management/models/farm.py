from django.db import models
from .company import Company


class Farm(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ферма'
        verbose_name_plural = 'Фермы'