from management.models import MilkYield
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm

from management.models.company import Company
from management.models.farm import Farm
from management.models.animal import Animal
from management.models.statistics.milk_yield import MilkYield
from django.contrib.admin import TabularInline, StackedInline


class MilkYieldAdmin(ModelAdmin):
    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True


    def has_delete_permission(self, request, obj=None):
        return True

    list_display = ('date', 'animal')

    # filter_horizontal = True
    list_filter = ('animal', 'date',)

    class Meta:
        model = MilkYield
