# Generated by Django 4.1.3 on 2022-11-18 08:41

from django.db import migrations, models
import uzlatekachny.models


class Migration(migrations.Migration):

    dependencies = [
        ('uzlatekachny', '0006_alter_food_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.AutoField(default=uzlatekachny.models.Food.next_id, primary_key=True, serialize=False),
        ),
    ]
