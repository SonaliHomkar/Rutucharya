# Generated by Django 2.2.5 on 2019-11-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealPlan', '0003_auto_20191128_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealdata',
            name='userId',
            field=models.IntegerField(blank=True),
        ),
    ]