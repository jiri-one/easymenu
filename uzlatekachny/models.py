from django.db import models
from djmoney.models.fields import MoneyField

class Food(models.Model):
    name = models.CharField("Food name", unique=True, max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    ingredients = models.TextField("Food ingredients", blank=True)
    notes = models.TextField("Food notes", blank=True)
    
    def __str__(self):
        return self.name
