from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Food, Category

class FoodAdmin(TranslationAdmin):
    pass
    
class CategoryAdmin(TranslationAdmin):
    pass

admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
