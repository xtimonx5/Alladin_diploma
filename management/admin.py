from django.conf.urls import url
from django.contrib import admin

# Management models
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

from .model_admins.rasschet import RasschetAdmin


# TODO: add groups
admin.site.unregister(Group)

# Register custom models
admin.site.register(Company, CompanyAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(AnimalType)
admin.site.register(Animal)
admin.site.register(Rasschet,RasschetAdmin)
admin.site.register(MilkYield, MilkYieldAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Norm, FoodAdmin)
admin.site.register(FarmGroup, FarmGroupAdmin)

