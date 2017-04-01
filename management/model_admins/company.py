from django.contrib.admin import ModelAdmin
from management.models.company import Company


class CompanyAdmin(ModelAdmin):
    class Meta:
        model = Company
