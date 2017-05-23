from django.contrib.admin import ModelAdmin
from django.http import HttpResponseRedirect

from management.models.company import Company
from management.models.food import Food
from django.contrib.admin import TabularInline, StackedInline
from django.core.urlresolvers import reverse
from django.utils.html import format_html


class FoodAdmin(ModelAdmin):
    list_display = ('name', 'calorie',)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
