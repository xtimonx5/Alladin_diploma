from django.contrib.admin import ModelAdmin
from django.forms import ModelForm

from management.models.company import Company
from management.models.farm import Farm
from management.models.animal import Animal
from management.models.statistics.milk_yield import MilkYield
from django.contrib.admin import TabularInline, StackedInline


class AnimalInline(TabularInline):
    model = Animal
    extra = 1
    # classes = ('grp-collapse grp-closed',)

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def yields_sum(self, obj):
        yield_objs = MilkYield.objects.filter(animal=obj)
        sum = 0
        for item in yield_objs:
            sum += item.weight
        return sum if yield_objs.exists() else '-'

    def yields_percent(self, obj):
        yield_objs = MilkYield.objects.filter(animal=obj)
        sum = 0.0
        for item in yield_objs:
            sum += item.weight
        return sum / yield_objs.count() if yield_objs.exists() else '-'

    readonly_fields = (
        'yields_sum',
        'yields_percent',
    )

    fields = (
        'type',
        'group',
        'name',
        'date_of_birth',
        'date_of_last_sex',
        'current_weight',
        'yields_sum',
        'yields_percent'
    )



class FarmAdmin(ModelAdmin):
    inlines = (
        AnimalInline,
    )

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Farm.objects.all()
        else:
            company = Company.objects.get(owner=request.user)
            return Farm.objects.filter(company=company)

    def krahmal_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.krahmal
        return need

    def calories_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.calories
        return need

    def sugar_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.sugar
        return need

    def calcii_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.calcii
        return need

    def fosfor_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.fosfor
        return need

    def magnie_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.magnie
        return need

    def cali_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.cali
        return need

    def sera_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.sera
        return need

    def jelezo_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.jelezo
        return need

    def med_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.med
        return need

    def cink_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.cink
        return need

    def marganec_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.marganec
        return need

    def kobalt_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.kobalt
        return need

    def iod_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.iod
        return need

    def karotin_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.med
        return need

    def vit_e_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.vit_e
        return need

    def vit_d_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.vit_d
        return need

    def vit_a_needs(self, obj):
        animals = Animal.objects.filter(farm=obj)
        need = 0
        # raise Exception
        for a in animals:
            need += a.type.vit_a
        return need

    readonly_fields = (
        'company',
        'calories_needs',
        'krahmal_needs',
        'sugar_needs',
        'calcii_needs',
        'fosfor_needs',
        'magnie_needs',
        'cali_needs',
        'sera_needs',
        'jelezo_needs',
        'med_needs',
        'cink_needs',
        'marganec_needs',
        'kobalt_needs',
        'iod_needs',
        'karotin_needs',
        'vit_e_needs',
        'vit_d_needs',
        'vit_a_needs'
    )
    # fields = (
    #     'company',
    #     'krahmal_needs',
    #     'name',
    # )
    fieldset_info = ('Standart_info', {'fields':
                                           ('company', 'name')
                                       })

    fieldset_needs = ('Needs', {'fields':
                                    ('calories_needs',
                                     'krahmal_needs',
                                     'sugar_needs',
                                     'calcii_needs',
                                     'fosfor_needs',
                                     'magnie_needs',
                                     'cali_needs',
                                     'sera_needs',
                                     'jelezo_needs',
                                     'med_needs',
                                     'cink_needs',
                                     'marganec_needs',
                                     'kobalt_needs',
                                     'iod_needs',
                                     'karotin_needs',
                                     'vit_e_needs',
                                     'vit_d_needs',
                                     'vit_a_needs',
                                     )
                                })

    fieldsets = (
        fieldset_info,
        fieldset_needs
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        field = super(FarmAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if request.user.is_superuser:
            return field
        if db_field.name == 'company':
            field.queryset = field.queryset.filter(owner=request.user)
        return field

    def has_delete_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        company = Company.objects.get(owner=request.user)
        obj.company = company
        return super(FarmAdmin, self).save_model(request, obj, form, change)

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    class Meta:
        model = Farm
