from django.contrib import admin
from modeltrans.admin import ActiveLanguageMixin
# internal imports
from .models import Food, Category

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    exclude = ['name', 'name_i18n']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['name', 'name_i18n']
