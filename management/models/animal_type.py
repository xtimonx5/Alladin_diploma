from django.db import models


class AnimalType(models.Model):
    name = models.CharField(max_length=50)
