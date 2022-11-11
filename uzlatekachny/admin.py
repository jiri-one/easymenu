from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Food, Category

for model in [Food, Category]:
    admin.site.register(model)

class FoodAdmin(TranslationAdmin):
    pass
    

class CategoryAdmin(TranslationAdmin):
    pass

admin.site.unregister(Food)
admin.site.unregister(Category)
admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
