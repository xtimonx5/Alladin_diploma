from django.db import models
from .company import Company


class Farm(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=50)
