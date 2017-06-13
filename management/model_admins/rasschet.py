from django.contrib.admin import ModelAdmin, StackedInline, TabularInline
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import format_html

from management.models.rasschet import Rasschet
from management.models.food import Food
from management.models.rasschet_foods import RasschetFood


class FoodInline(TabularInline):
    model = RasschetFood
    extra = 1

    def percent(self, obj):
        current_calorie = obj.food.calorie * obj.count
        all_calorie = RasschetFood.objects.filter(rasschet=obj.rasschet)
        all = 0
        for item in all_calorie:
            all += item.food.calorie * item.count

        return str(current_calorie / all * 100) + '%'

    readonly_fields = ('percent',)

    fields = (
        'food',
        'count',
        'percent',
    )
    verbose_name = 'Корм'
    verbose_name_plural = 'Корма'


class RasschetAdmin(ModelAdmin):
    inlines = (
        FoodInline,
    )

    @staticmethod
    def get_racion(obj, field_value):
        all_foods = RasschetFood.objects.filter(rasschet=obj)
        value = 0
        for item in all_foods:
            value += getattr(item.food, field_value) * item.count
        return round(value, 2)

    @staticmethod
    def get_balance(obj, field_value):
        return round(RasschetAdmin.get_racion(obj, field_value) - getattr(obj.norm, field_value))

    @staticmethod
    def get_percent(obj, field_value):
        try:
            return str(round(RasschetAdmin.get_balance(obj, field_value) * 100 / getattr(obj.norm, field_value),2)) + '%'
        except:
            return '0 %'

    def rasschet(self, obj):
        corm = dict(
            racion=self.get_racion(obj, 'corm'),
            norm=obj.norm.corm,
            balance=self.get_balance(obj, 'corm'),
            percent=self.get_percent(obj, 'corm')
        )
        obmen_energ = dict(
            racion=self.get_racion(obj, 'calorie'),
            norm=obj.norm.calorie,
            balance=self.get_balance(obj, 'calorie'),
            percent=self.get_percent(obj, 'calorie')
        )
        suh_veschescto = dict(
            racion=self.get_racion(obj, 'suh_veschestvo'),
            norm=obj.norm.suh_veschestvo,
            balance=self.get_balance(obj, 'suh_veschestvo'),
            percent=self.get_percent(obj, 'suh_veschestvo')
        )
        sir_proteine = dict(
            racion=self.get_racion(obj, 'Siro_proteine'),
            norm=obj.norm.Siro_proteine,
            balance=self.get_balance(obj, 'Siro_proteine'),
            percent=self.get_percent(obj, 'Siro_proteine')
        )
        perev_proteine = dict(
            racion=self.get_racion(obj, 'Perev_proteine'),
            norm=obj.norm.Perev_proteine,
            balance=self.get_balance(obj, 'Perev_proteine'),
            percent=self.get_percent(obj, 'Perev_proteine')
        )
        sir_jir = dict(
            racion=self.get_racion(obj, 'sir_jir'),
            norm=obj.norm.sir_jir,
            balance=self.get_balance(obj, 'sir_jir'),
            percent=self.get_percent(obj, 'sir_jir')
        )
        sir_cletchatka = dict(
            racion=self.get_racion(obj, 'sir_cletchatka'),
            norm=obj.norm.sir_cletchatka,
            balance=self.get_balance(obj, 'sir_cletchatka'),
            percent=self.get_percent(obj, 'sir_cletchatka')
        )
        krahmal = dict(
            racion=self.get_racion(obj, 'krahmal'),
            norm=obj.norm.krahmal,
            balance=self.get_balance(obj, 'krahmal'),
            percent=self.get_percent(obj, 'krahmal')
        )
        sugar = dict(
            racion=self.get_racion(obj, 'sugar'),
            norm=obj.norm.sugar,
            balance=self.get_balance(obj, 'sugar'),
            percent=self.get_percent(obj, 'sugar')
        )
        sol = dict(
            racion=self.get_racion(obj, 'sol'),
            norm=obj.norm.sol,
            balance=self.get_balance(obj, 'sol'),
            percent=self.get_percent(obj, 'sol')
        )
        calci = dict(
            racion=self.get_racion(obj, 'calcii'),
            norm=obj.norm.calcii,
            balance=self.get_balance(obj, 'calcii'),
            percent=self.get_percent(obj, 'calcii')
        )
        fosfor = dict(
            racion=self.get_racion(obj, 'fosfor'),
            norm=obj.norm.fosfor,
            balance=self.get_balance(obj, 'fosfor'),
            percent=self.get_percent(obj, 'fosfor')
        )
        magnie = dict(
            racion=self.get_racion(obj, 'magnie'),
            norm=obj.norm.magnie,
            balance=self.get_balance(obj, 'magnie'),
            percent=self.get_percent(obj, 'magnie')
        )
        cali = dict(
            racion=self.get_racion(obj, 'cali'),
            norm=obj.norm.cali,
            balance=self.get_balance(obj, 'cali'),
            percent=self.get_percent(obj, 'cali')
        )
        sera = dict(
            racion=self.get_racion(obj, 'sera'),
            norm=obj.norm.sera,
            balance=self.get_balance(obj, 'sera'),
            percent=self.get_percent(obj, 'sera')
        )
        jelezo = dict(
            racion=self.get_racion(obj, 'jelezo'),
            norm=obj.norm.jelezo,
            balance=self.get_balance(obj, 'jelezo'),
            percent=self.get_percent(obj, 'jelezo')
        )
        natrie = dict(
            racion=self.get_racion(obj, 'natri'),
            norm=obj.norm.natri,
            balance=self.get_balance(obj, 'natri'),
            percent=self.get_percent(obj, 'natri')
        )
        med = dict(
            racion=self.get_racion(obj, 'med'),
            norm=obj.norm.med,
            balance=self.get_balance(obj, 'med'),
            percent=self.get_percent(obj, 'med')
        )
        cink = dict(
            racion=self.get_racion(obj, 'cink'),
            norm=obj.norm.cink,
            balance=self.get_balance(obj, 'cink'),
            percent=self.get_percent(obj, 'cink')
        )
        marganec = dict(
            racion=self.get_racion(obj, 'marganec'),
            norm=obj.norm.marganec,
            balance=self.get_balance(obj, 'marganec'),
            percent=self.get_percent(obj, 'marganec')
        )
        kobalt = dict(
            racion=self.get_racion(obj, 'kobalt'),
            norm=obj.norm.kobalt,
            balance=self.get_balance(obj, 'kobalt'),
            percent=self.get_percent(obj, 'kobalt')
        )
        iod = dict(
            racion=self.get_racion(obj, 'iod'),
            norm=obj.norm.iod,
            balance=self.get_balance(obj, 'iod'),
            percent=self.get_percent(obj, 'iod')
        )
        karotin = dict(
            racion=self.get_racion(obj, 'karotin'),
            norm=obj.norm.karotin,
            balance=self.get_balance(obj, 'karotin'),
            percent=self.get_percent(obj, 'karotin')
        )
        vit_d = dict(
            racion=self.get_racion(obj, 'vit_d'),
            norm=obj.norm.vit_d,
            balance=self.get_balance(obj, 'vit_d'),
            percent=self.get_percent(obj, 'vit_d')
        )
        vit_e = dict(
            racion=self.get_racion(obj, 'vit_e'),
            norm=obj.norm.vit_e,
            balance=self.get_balance(obj, 'vit_e'),
            percent=self.get_percent(obj, 'vit_e')
        )
        vit_a = dict(
            racion=self.get_racion(obj, 'vit_a'),
            norm=obj.norm.vit_a,
            balance=self.get_balance(obj, 'vit_a'),
            percent=self.get_percent(obj, 'vit_a')
        )

        context = dict(
            corm=corm,
            obmen_energ=obmen_energ,
            suh_veschescto=suh_veschescto,
            sir_proteine=sir_proteine,
            perev_proteine=perev_proteine,
            sir_jir=sir_jir,
            sir_cletchatka=sir_cletchatka,
            krahmal=krahmal,
            sugar=sugar,
            sol=sol,
            calci=calci,
            fosfor=fosfor,
            magnie=magnie,
            cali=cali,
            sera=sera,
            jelezo=jelezo,
            natrie=natrie,
            med=med,
            cink=cink,
            marganec=marganec,
            kobalt=kobalt,
            iod=iod,
            karotin=karotin,
            vit_d=vit_d,
            vit_e=vit_e,
            vit_a=vit_a
        )

        html = render_to_string('rasschet_field.html', context=context)
        html = format_html(html)
        return html

    list_display = (
        'farm',
        'group',
        'year',
        'month',
        'norm',

    )

    fields = (
        'farm',
        'month',
        'year',
        'group',
        'type',
        'norm',
        'rasschet'
    )
    readonly_fields = ('rasschet',)
