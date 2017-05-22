from django.db import models


class AnimalType(models.Model):
    name = models.CharField(max_length=50)
    # Norms
    calories =  models.IntegerField(null=True,blank=True,default=0)
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

    # Cost
    cost = models.IntegerField(null=True,blank=True, default=0)

    def __str__(self):
        return self.name