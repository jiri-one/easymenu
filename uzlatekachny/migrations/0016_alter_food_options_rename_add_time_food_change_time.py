# Generated by Django 4.1.3 on 2022-11-21 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uzlatekachny', '0015_alter_food_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['order', '-change_time']},
        ),
        migrations.RenameField(
            model_name='food',
            old_name='add_time',
            new_name='change_time',
        ),
    ]