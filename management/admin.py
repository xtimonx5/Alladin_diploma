from django.conf.urls import url
from django.contrib import admin

# Management models
from django.contrib.admin import ModelAdmin
from django.shortcuts import redirect
from django.urls import reverse

from management.model_admins.farm_group import FarmGroupAdmin
from .models.company import Company
from .models.farm import Farm
from .models.animal import Animal
from .models.animal_type import AnimalType
# from .model_admins.animal import AnimalModelAdmin
from .model_admins.company import CompanyAdmin
from .model_admins.farm import FarmAdmin
from .model_admins.yields import MilkYieldAdmin, MilkYield
from django.contrib.auth.models import User, Group
from .models.food import Food
from .model_admins.food import FoodAdmin
from .models import FarmGroup
# from .models.farm_group import FarmGroup
from .models import Norm
from .models.rasschet import Rasschet
from django.template.loader import render_to_string
from django.utils.html import format_html

from .model_admins.rasschet import RasschetAdmin


class Zatrat(Company):
    class Meta:
        proxy = True
        verbose_name = 'Кормовая затрата'
        verbose_name_plural = 'Кормовые затраты'


class ZatratAdmin(ModelAdmin):
    def zatrati(self, obj):
        context = {}
        html = render_to_string('food_table_2.html', context=context)
        html = format_html(html)
        return html


    def year(self, obj):
        return '2017'

    fields = ('name', 'year','zatrati',)
    readonly_fields = ('name', 'year','zatrati',)


    # def get_list_display(self, request):
    #     if not request.user.is_superuser:
    #         return super(ZatratAdmin, self).get_list_display(request)
    #     else:
    #         company = Company.objects.get(owner=request.user)
    #         url = reverse('admin:%s_%s_change' % ('management',
    #                                               'zatrat'),
    #                       args=(company.id,))
    #         # raise Exception
    #         return redirect(url)
    #         # return format_html(u'<a href="{}">{}</a>', (url), 'Change  ' + obj.name)



# TODO: add groups
admin.site.unregister(Group)
admin.site.register(Zatrat, ZatratAdmin)
# Register custom models
admin.site.register(Company, CompanyAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(AnimalType)
admin.site.register(Animal)
admin.site.register(Rasschet, RasschetAdmin)
admin.site.register(MilkYield, MilkYieldAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Norm, FoodAdmin)
admin.site.register(FarmGroup, FarmGroupAdmin)
