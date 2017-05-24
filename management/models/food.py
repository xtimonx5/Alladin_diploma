from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)

    сorm = models.FloatField(verbose_name='Корм')
    calorie = models.FloatField(verbose_name='Обмен энергией')
    suh_veschestvo = models.FloatField(null=True, blank=True, default=0, verbose_name='Сухое вещество')
    Siro_proteine = models.FloatField(null=True, blank=True, default=0, verbose_name='Сырой протеин')
    Perev_proteine = models.FloatField(null=True, blank=True, default=0, verbose_name='Переваренный протеин')
    sir_jir = models.FloatField(null=True, blank=True, default=0, verbose_name='Сыр жир')
    sir_cletchatka = models.FloatField(null=True, blank=True, default=0, verbose_name='Сыр клетчатка')

    krahmal = models.FloatField(null=True, blank=True, default=0, verbose_name='Крахмал')
    sugar = models.FloatField(null=True, blank=True, default=0, verbose_name='Сахар')
    sol = models.FloatField(null=True, blank=True, default=0, verbose_name='Соль')

    calcii = models.FloatField(null=True, blank=True, default=0, verbose_name='Кальций')
    fosfor = models.FloatField(null=True, blank=True, default=0, verbose_name='Фосфор')
    magnie = models.FloatField(null=True, blank=True, default=0, verbose_name='Магний')
    cali = models.FloatField(null=True, blank=True, default=0, verbose_name='Калий')
    sera = models.FloatField(null=True, blank=True, default=0, verbose_name='Сера')
    jelezo = models.FloatField(null=True, blank=True, default=0, verbose_name='Железо')
    natri = models.FloatField(null=True, blank=True, default=0, verbose_name='Натрий')
    med = models.FloatField(null=True, blank=True, default=0, verbose_name='Медь')
    cink = models.FloatField(null=True, blank=True, default=0, verbose_name='Цинк')
    marganec = models.FloatField(null=True, blank=True, default=0, verbose_name='Марганец')
    kobalt = models.FloatField(null=True, blank=True, default=0, verbose_name='Кобальт ')
    iod = models.FloatField(null=True, blank=True, default=0, verbose_name='Йод')
    karotin = models.FloatField(null=True, blank=True, default=0, verbose_name='Каротин')

    vit_e = models.FloatField(null=True, blank=True, default=0, verbose_name='Витамин Е')
    vit_d = models.FloatField(null=True, blank=True, default=0, verbose_name='Витамин Д')
    vit_a = models.FloatField(null=True, blank=True, default=0, verbose_name='Витамин А')

    def __str__(self):
        return self.name
