from django.contrib import admin
from .models import UnitDatasheet, List, Wargear

# Register your models here.

admin.site.register(UnitDatasheet)
admin.site.register(Wargear)
admin.site.register(List)
