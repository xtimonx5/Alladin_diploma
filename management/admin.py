from django.contrib import admin

# Management models
from .models.company import Company
from .models.farm import Farm
from .models.animal import Animal
from .models.animal_type import AnimalType

from .model_admins.company import CompanyAdmin
from .model_admins.farm import FarmAdmin
from .model_admins.yields import MilkYieldAdmin, MilkYield
from django.contrib.auth.models import User, Group
from .models.food import Food
from .model_admins.food import FoodAdmin

# TODO: add groups
admin.site.unregister(Group)

# Register custom models
admin.site.register(Company, CompanyAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(AnimalType)
admin.site.register(Animal)
admin.site.register(MilkYield, MilkYieldAdmin)
admin.site.register(Food, FoodAdmin)

# Register your models here.
