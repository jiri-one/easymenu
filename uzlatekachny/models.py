from django.db import models
from django.core.validators import MinValueValidator
# imports of external Django modules
from djmoney.models.fields import MoneyField
from modeltrans.fields import TranslationField

class Food(models.Model):
    def get_next_id(): # type: ignore
        return Food.objects.count() + 1
    id = models.IntegerField(primary_key=True, validators=[MinValueValidator(1)], editable=True, default=get_next_id)
    name = models.CharField("Food name", unique=True, max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='CZK')
    ingredients = models.CharField("Food ingredients", blank=True, max_length=200)
    notes = models.CharField("Food notes", blank=True, max_length=200)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    i18n = TranslationField(fields=("name", "ingredients", "notes"))
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pk"]

class Category(models.Model):
    def get_next_id(): # type: ignore
        return Category.objects.count() + 1
    id = models.IntegerField(primary_key=True, validators=[MinValueValidator(1)], editable=True, default=get_next_id)
    name = models.CharField("Food category name", unique=True, max_length=100)
    i18n = TranslationField(fields=("name", ))
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pk"]
