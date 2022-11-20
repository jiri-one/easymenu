from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# imports of external Django modules
from djmoney.models.fields import MoneyField
from modeltrans.fields import TranslationField

class Food(models.Model):  
    def next_order_nr(): # type: ignore
        return Food.objects.last().order + 1
    
    def next_id(): # type: ignore
        return Food.objects.last().id + 1
    
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
    add_time = models.DateTimeField(auto_now=True)
    i18n = TranslationField(fields=("name", "ingredients", "notes"))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._prev_order = self.order
    
    def __str__(self):
        return self.name
           
    class Meta:
        ordering = ["order", "-add_time"]
    
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
def change_order_is_save_same(sender, instance, **kwargs):
    same = sender.objects.filter(order=instance.order).count()
    if same > 1:
        # if previous value of order is lower or higher, I can only switch the values
        if instance._prev_order in [instance.order+1, instance.order-1]:
            sec_food = sender.objects.filter(order=instance.order).exclude(pk=instance.pk)[0]
            sender.objects.filter(pk=sec_food.pk).update(order=instance._prev_order)

        
@receiver(post_delete, sender=Food)
def change_order_if_delete(sender, instance, **kwargs):
    if sender.objects.count() != instance.order:
        Food.refresh_order()
