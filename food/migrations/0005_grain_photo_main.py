# Generated by Django 2.2.5 on 2019-09-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20190924_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='grain',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]