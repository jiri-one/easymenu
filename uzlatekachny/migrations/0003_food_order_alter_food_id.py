# Generated by Django 4.1.3 on 2022-11-17 16:41

import django.core.validators
from django.db import migrations, models
import uzlatekachny.models


class Migration(migrations.Migration):

    dependencies = [
        ('uzlatekachny', '0002_alter_food_ingredients_alter_food_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='order',
            field=models.IntegerField(default=uzlatekachny.models.Food.get_next_order_nr, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
