from models import FoodOption
from django.contrib import admin

class FoodOptionAdmin(admin.ModelAdmin):
    pass

admin.site.register(FoodOption, FoodOptionAdmin)