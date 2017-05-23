from django.db import models


class FarmGroup(models.Model):
    name = models.CharField(max_length=200)
    farm = models.ForeignKey('Farm')

    def __str__(self):
        return self.name