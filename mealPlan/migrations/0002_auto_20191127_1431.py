# Generated by Django 2.2.5 on 2019-11-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealPlan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='mealDate',
            field=models.DateField(blank=True),
        ),
    ]
