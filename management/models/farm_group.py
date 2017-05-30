from django.db import models


class FarmGroup(models.Model):
    name = models.CharField(max_length=200)
    farm = models.ForeignKey('Farm')
    # type = models.ForeignKey('AnimalType', null=True, blank=True)

    def __str__(self):
        return self.farm.name + '/' + self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'