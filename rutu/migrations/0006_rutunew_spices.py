# Generated by Django 2.2.5 on 2019-10-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_drinks_fruitjuices_fruits_leafyveg_lentils_nonveg_soup_spices_vegetables'),
        ('rutu', '0005_auto_20191001_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutunew',
            name='spices',
            field=models.ManyToManyField(related_name='spices', to='food.spices'),
        ),
    ]
