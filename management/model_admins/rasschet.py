from django.contrib.admin import ModelAdmin, StackedInline, TabularInline
from django.db.models import Sum
from django.http import HttpResponseRedirect
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
            all += item.food.calorie*item.count
        return str(current_calorie/all*100) + '%'

    readonly_fields = ('percent',)

    fields = (
        'food',
        'count',
        'percent',
    )


class RasschetAdmin(ModelAdmin):
    inlines = (
        FoodInline,
    )
    # fieldset_rasschet_contains = ('В рационе содержится', {'fields':('corm_ed',
    #                                                                  'obmen_energ',
    #                                                                  'suh_veschestvo',
    #                                                                  'sir_proteine',
    #                                                                  'perev_proteine',
    #                                                                  'sir_jir',
    #                                                                  'sir_cletchatka',
    #                                                                  'krahmal',
    #                                                                  'sugar',
    #                                                                  'calcii',
    #                                                                  'fosfor',
    #                                                                  'magni',
    #                                                                  'calii',
    #                                                                  'sera',
    #                                                                  'jelezo',
    #                                                                  'med',
    #                                                                  'cink',
    #                                                                  'marganec',
    #                                                                  'kobalt',
    #                                                                  'iod',
    #                                                                  'karotin',
    #                                                                  'vit_d',
    #                                                                  'vit_e'
    #                                                                  )
    #                                                        })
    # fields = (
    #     '',
    #     '',
    # )
