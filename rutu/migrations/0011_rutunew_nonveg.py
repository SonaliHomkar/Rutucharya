# Generated by Django 2.2.5 on 2019-10-04 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_drinks_fruitjuices_fruits_leafyveg_lentils_nonveg_soup_spices_vegetables'),
        ('rutu', '0010_rutunew_soup'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutunew',
            name='nonVeg',
            field=models.ManyToManyField(related_name='nonVeg', to='food.nonVeg'),
        ),
    ]
