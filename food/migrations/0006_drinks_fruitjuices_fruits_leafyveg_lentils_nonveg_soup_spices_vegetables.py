# Generated by Django 2.2.5 on 2019-09-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_grain_photo_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='drinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drinkName', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='fruitJuices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruitJuiceName', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='fruits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruitName', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='leafyveg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leafyVegName', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='lentils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lentilName', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='nonVeg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nonVegName', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='soup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soupName', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='spices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spiceName', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='vegetables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegName', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]
