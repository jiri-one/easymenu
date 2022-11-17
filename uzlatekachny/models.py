from django.db import models
from django.core.validators import MinValueValidator
# imports of external Django modules
from djmoney.models.fields import MoneyField
from modeltrans.fields import TranslationField

class Food(models.Model):
    def get_next_order_nr(): # type: ignore
        return Food.objects.last().order + 1
    name = models.CharField("Food name", unique=True, max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='CZK')
    ingredients = models.CharField("Food ingredients", blank=True, null=True, max_length=200)
    notes = models.CharField("Food notes", blank=True, null=True, max_length=200)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    order = models.IntegerField(
        validators=[MinValueValidator(1)],                      default=get_next_order_nr)
    i18n = TranslationField(fields=("name", "ingredients", "notes"))
    
    def __str__(self):
        return self.name
    
    
    # def save(self, *args, **kwargs):
    #     if self.id in Food.objects.all().values_list('id', flat=True):
    #         for food in Food.objects.filter(id__gte=self.id).order_by("-id"):
    #             food.id += 1
    #             food.save()
    #     super().save(*args, **kwargs)

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
