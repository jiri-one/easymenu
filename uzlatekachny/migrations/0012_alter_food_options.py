# Generated by Django 4.1.3 on 2022-11-20 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uzlatekachny', '0011_alter_food_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['order', 'add_time']},
        ),
    ]
