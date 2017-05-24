from django.db import models


class Norm(models.Model):
    name = models.CharField(max_length=100)
    animal_type = models.ForeignKey('AnimalType')
    # norms

    calorie = models.IntegerField()
    suh_veschestvo = models.IntegerField(null=True,blank=True, default=0)
    Siro_proteine = models.IntegerField(null=True,blank=True, default=0)
    Perev_proteine = models.IntegerField(null=True,blank=True, default=0, verbose_name='Переваренный протеин')
    sir_jir = models.IntegerField(null=True,blank=True, default=0)
    sir_cletchatka = models.IntegerField(null=True,blank=True, default=0, verbose_name='Сыр клетчатка')
    sol = models.IntegerField(null=True,blank=True, default=0, verbose_name='Соль')

    krahmal = models.IntegerField(null=True, blank=True, default=0)
    sugar = models.IntegerField(null=True, blank=True, default=0)

    calcii = models.IntegerField(null=True, blank=True, default=0)
    fosfor = models.IntegerField(null=True, blank=True, default=0)
    magnie = models.IntegerField(null=True, blank=True, default=0)
    cali = models.IntegerField(null=True, blank=True, default=0)
    sera = models.IntegerField(null=True, blank=True, default=0)
    jelezo = models.IntegerField(null=True, blank=True, default=0)
    med = models.IntegerField(null=True, blank=True, default=0)
    cink = models.IntegerField(null=True, blank=True, default=0)
    marganec = models.IntegerField(null=True, blank=True, default=0)
    kobalt = models.IntegerField(null=True, blank=True, default=0)
    iod = models.IntegerField(null=True, blank=True, default=0)
    karotin = models.IntegerField(null=True, blank=True, default=0)

    vit_e = models.IntegerField(null=True, blank=True, default=0)
    vit_d = models.IntegerField(null=True, blank=True, default=0)
    vit_a = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name