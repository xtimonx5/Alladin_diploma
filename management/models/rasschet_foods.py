from django.db import models


class RasschetFood(models.Model):
    rasschet = models.ForeignKey('Rasschet')
    food = models.ForeignKey('Food')
    count = models.FloatField()