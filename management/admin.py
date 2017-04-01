from django.contrib import admin

# Management models
from .models.company import Company
from .model_admins.company import CompanyAdmin

admin.site.register(Company, CompanyAdmin)

# Register your models here.
