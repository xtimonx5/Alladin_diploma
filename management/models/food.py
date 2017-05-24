from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)

    сorm = models.FloatField(verbose_name='Корм')
    calorie = models.FloatField(verbose_name='Обмен энергией КРС')
    calorie_с = models.FloatField(verbose_name='Обмен энергией С')
    calorie_o = models.FloatField(verbose_name='Обмен энергией O')
    suh_veschestvo = models.FloatField(null=True, blank=True, default=0, verbose_name='Сухое вещество')
    Siro_proteine = models.FloatField(null=True, blank=True, default=0, verbose_name='Сырой протеин')
    Perev_proteine = models.FloatField(null=True, blank=True, default=0, verbose_name='Переваренный протеин')
    sir_jir = models.FloatField(null=True, blank=True, default=0, verbose_name='Сыр жир')
    sir_cletchatka = models.FloatField(null=True, blank=True, default=0, verbose_name='Сыр клетчатка')
    bev = models.FloatField(null=True, blank=True, default=0, verbose_name='БЭВ')
    krahmal = models.FloatField(null=True, blank=True, default=0, verbose_name='Крахмал')
    sugar = models.FloatField(null=True, blank=True, default=0, verbose_name='Сахар')
    lizin = models.FloatField(null=True, blank=True, default=0, verbose_name='Лизин')
    mecionin_cistin = models.FloatField(null=True, default=0, verbose_name='Метионин + Цистин')
    sol = models.FloatField(null=True, blank=True, default=0, verbose_name='Соль')

    calcii = models.FloatField(null=True, blank=True, default=0, verbose_name='Кальций')
    fosfor = models.FloatField(null=True, blank=True, default=0, verbose_name='Фосфор')
    magnie = models.FloatField(null=True, blank=True, default=0, verbose_name='Магний')
    cali = models.FloatField(null=True, blank=True, default=0, verbose_name='Калий')
    natri = models.FloatField(null=True, blank=True, default=0, verbose_name='Натрий')
    hlor = models.FloatField(null=True, blank=True, default=0, verbose_name='Хлор')
    sera = models.FloatField(null=True, blank=True, default=0, verbose_name='Сера')
    jelezo = models.FloatField(null=True, blank=True, default=0, verbose_name='Железо')
    med = models.FloatField(null=True, blank=True, default=0, verbose_name='Медь')
    cink = models.FloatField(null=True, blank=True, default=0, verbose_name='Цинк')
    marganec = models.FloatField(null=True, blank=True, default=0, verbose_name='Марганец')
    kobalt = models.FloatField(null=True, blank=True, default=0, verbose_name='Кобальт ')
    iod = models.FloatField(null=True, blank=True, default=0, verbose_name='Йод')
    karotin = models.FloatField(null=True, blank=True, default=0, verbose_name='Каротин')

    vit_a = models.FloatField(null=True, blank=True, default=0, verbose_name='Витамин А')
    vit_d = models.FloatField(null=True, blank=True, default=0, verbose_name='Витамин Д')
    vit_e = models.FloatField(null=True, blank=True, default=0, verbose_name='Витамин Е')

    def __str__(self):
        return self.name
