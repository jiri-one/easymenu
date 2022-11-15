from django.contrib import admin
from modeltrans.admin import ActiveLanguageMixin
# internal imports
from .models import Food, Category

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name_cs', 'name_en', 'name_de', 'name_ru')
        }),
        ('Add ingredients', {
            'classes': ('collapse',),
            'fields': ('ingredients_cs', 'ingredients_en', 'ingredients_de', 'ingredients_ru'),
        }),
        ('Add notes', {
            'classes': ('collapse',),
            'fields': ('notes_cs', 'notes_en', 'notes_de', 'notes_ru'),
        })
    )
    #exclude = ['name', 'name_i18n', 'ingredients', 'ingredients_i18n','notes', 'notes_i18n']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['name', 'name_i18n']
