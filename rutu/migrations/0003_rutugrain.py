# Generated by Django 2.2.5 on 2019-09-30 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_drinks_fruitjuices_fruits_leafyveg_lentils_nonveg_soup_spices_vegetables'),
        ('rutu', '0002_auto_20190920_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='RutuGrain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rutu.Rutu')),
                ('grain', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='food.grain')),
            ],
        ),
    ]
