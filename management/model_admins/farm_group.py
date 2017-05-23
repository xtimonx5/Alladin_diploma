from django.contrib.admin import ModelAdmin
from django.http import HttpResponseRedirect

from management.models.company import Company
from management.models.farm import Farm
from management.models.animal import Animal
from django.contrib.admin import TabularInline, StackedInline
from django.core.urlresolvers import reverse
from django.utils.html import format_html


class FarmGroupAdmin(ModelAdmin):
    def has_module_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True
