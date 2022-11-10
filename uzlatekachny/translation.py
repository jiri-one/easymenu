from modeltranslation.translator import translator, TranslationOptions
from .models import Food, Category

class FoodTranslationOptions(TranslationOptions):
    fields = ('name', 'ingredients', 'notes')

translator.register(Food, FoodTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)
