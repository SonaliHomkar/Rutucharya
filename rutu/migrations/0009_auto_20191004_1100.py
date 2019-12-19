# Generated by Django 2.2.5 on 2019-10-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_drinks_fruitjuices_fruits_leafyveg_lentils_nonveg_soup_spices_vegetables'),
        ('rutu', '0008_rutunew_fruitjuices'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutunew',
            name='drinks',
            field=models.ManyToManyField(related_name='drinks', to='food.drinks'),
        ),
        migrations.AddField(
            model_name='rutunew',
            name='leafyveg',
            field=models.ManyToManyField(related_name='leafyveg', to='food.leafyveg'),
        ),
        migrations.AddField(
            model_name='rutunew',
            name='lentils',
            field=models.ManyToManyField(related_name='lentils', to='food.lentils'),
        ),
        migrations.AddField(
            model_name='rutunew',
            name='vegetables',
            field=models.ManyToManyField(related_name='vegetables', to='food.vegetables'),
        ),
    ]
