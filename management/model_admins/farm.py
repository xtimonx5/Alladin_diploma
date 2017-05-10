from django.contrib.admin import ModelAdmin
from django.forms import ModelForm

from management.models.company import Company
from management.models.farm import Farm
from management.models.animal import Animal
from management.models.statistics.milk_yield import MilkYield
from django.contrib.admin import TabularInline, StackedInline


class AnimalInline(TabularInline):
    model = Animal
    extra = 0

    def yields_sum(self, obj):
        yield_objs = MilkYield.objects.filter(animal=obj)
        sum = 0
        for item in yield_objs:
            sum += item.weight
        return sum if yield_objs.exists() else '-'

    def yields_percent(self,obj):
        yield_objs = MilkYield.objects.filter(animal=obj)
        sum = 0.0
        for item in yield_objs:
            sum += item.weight
        return sum/yield_objs.count() if yield_objs.exists() else '-'

    readonly_fields = (
        'yields_sum',
        'yields_percent'
    )

    fields = (
        'type',
        'name',
        'date_of_birth',
        'date_of_last_sex',
        'current_weight',
        'yields_sum',
        'yields_percent'
    )

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


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

    readonly_fields = (
        'company',

    )
    fields = (
        'company',
        'name',
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
