# Generated by Django 2.2.5 on 2019-10-03 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_drinks_fruitjuices_fruits_leafyveg_lentils_nonveg_soup_spices_vegetables'),
        ('rutu', '0006_rutunew_spices'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutunew',
            name='fruits',
            field=models.ManyToManyField(related_name='fruits', to='food.fruits'),
        ),
    ]