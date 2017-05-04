from django.contrib import admin

# Management models
from .models.company import Company
from .models.farm import Farm
from .models.animal import Animal
from .models.animal_type import AnimalType

from .model_admins.company import CompanyAdmin
from .model_admins.farm import FarmAdmin
from django.contrib.auth.models import User, Group

# from .model_admins.user import UserAdmin

# TODO: add groups
admin.site.unregister(Group)

# Register custom models
admin.site.register(Company, CompanyAdmin)
admin.site.register(Farm, FarmAdmin)
admin.site.register(AnimalType)
admin.site.register(Animal)



# Register your models here.
