from django.db import models

class Food(models.Model):
    name = models.CharField("Food name", unique=True, max_length=100)
    price = models.
    
