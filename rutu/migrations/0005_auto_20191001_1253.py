# Generated by Django 2.2.5 on 2019-10-01 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutu', '0004_rutunew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutunew',
            name='grain',
            field=models.ManyToManyField(related_name='grain', to='food.grain'),
        ),
    ]