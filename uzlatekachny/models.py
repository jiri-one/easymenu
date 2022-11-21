from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# imports of external Django modules
from djmoney.models.fields import MoneyField
from modeltrans.fields import TranslationField

class Food(models.Model):  
    def next_order_nr(): # type: ignore
        return Food.objects.last().order + 1
    
    def next_id(): # type: ignore
        return Food.objects.count() + 1
    
    @staticmethod
    def refresh_order(): # type: ignore
        def order_nr_generator():
            for number in range(1, Food.objects.count()+1):
                yield number
            
        counter = order_nr_generator()
        
        for food in Food.objects.all():
            Food.objects.filter(pk=food.pk).update(order=next(counter))

    id = models.AutoField(primary_key=True, default=next_id)
    name = models.CharField("Food name", unique=True, max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='CZK')
    ingredients = models.CharField("Food ingredients", blank=True, null=True, max_length=200)
    notes = models.CharField("Food notes", blank=True, null=True, max_length=200)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    order = models.IntegerField(unique=False, default=next_order_nr)
    change_time = models.DateTimeField(auto_now=True)
    i18n = TranslationField(fields=("name", "ingredients", "notes"))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._prev_order = self.order
        if hasattr(self, "category"):
            self._prev_category = self.category
    
    def __str__(self):
        return self.name
       
    def clean(self, *args, **kwargs):
        if hasattr(self, "category") and hasattr(self, "order"):
            cat_values = list(self.category.food_set.values_list("order", flat=True))
            new_in_cat = 1
            if hasattr(self, "_prev_category"):
                if self._prev_category == self.category:
                    new_in_cat = 0 # I don't need to add next order nr. if only move food in the same category
            if not (cat_values[0] <= self.order <= cat_values[-1] + new_in_cat):
                raise ValidationError({'order': f"Číslo musí být mezi {cat_values[0]} a {cat_values[-1] + new_in_cat} nebo zvolte jinou kategorii!"})
           
    class Meta:
        ordering = ["order", "-change_time"]
    
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

@receiver(post_save, sender=Food)
def change_order_if_save_same(sender, instance, **kwargs):
    same = sender.objects.filter(order=instance.order).count()
    if same > 1:
        # if previous value of order is +-1, I can only switch the values
        if instance._prev_order in [instance.order+1, instance.order-1]:
            # get second food with same order number
            sec_food = sender.objects.filter(order=instance.order).exclude(pk=instance.pk)[0]
            # update second food order number to previous value from actual food
            sender.objects.filter(pk=sec_food.pk).update(order=instance._prev_order)
        # if I change order to higher number (more in the list below) I have to +1,
        # because the changed order is always first in the list (when two same order numbers)
        # that's because of ordering = ["order", "-change_time"], -change_time is second ordering
        elif (instance.order - instance._prev_order) >= 2:
            sender.objects.filter(pk=instance.pk).update(order=instance.order+1)
            sender.refresh_order()
        # if I change order to lower number (higher in list), then it is OK and I can only refresh_order()
        else:
            sender.refresh_order()

@receiver(post_delete, sender=Food)
def change_order_if_delete(sender, instance, **kwargs):
    if sender.objects.count() != instance.order:
        sender.refresh_order()
