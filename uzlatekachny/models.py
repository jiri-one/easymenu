from django.db import models
from djmoney.models.fields import MoneyField
from modeltrans.fields import TranslationField

class Food(models.Model):
    name = models.CharField("Food name", unique=True, max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    ingredients = models.TextField("Food ingredients", blank=True)
    notes = models.TextField("Food notes", blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    i18n = TranslationField(fields=("name", "ingredients", "notes"))
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pk"]

class Category(models.Model):
    name = models.CharField("Food category name", unique=True, max_length=100)
    i18n = TranslationField(fields=("name", ))
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pk"]
