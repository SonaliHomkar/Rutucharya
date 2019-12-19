from django.db import models
from datetime import datetime
from food.models import Excercise, food, foodType, grain, spices,fruits,fruitJuices
from food.models import vegetables, leafyveg,drinks, lentils, soup, nonVeg, legumes

 




# Create your models here.
class Zone(models.Model):
    zone = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.zone

class Rutu(models.Model):
    Name = models.CharField(max_length=300)
    zone = models.ForeignKey(Zone,on_delete = models.DO_NOTHING)
    description = models.TextField(blank=True)
    fromDate = models.DateTimeField(default = datetime.now)
    toDate = models.DateTimeField(default = datetime.now)
    allowedDescr = models.TextField(blank=True)
    notAllowedDescr = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return self.Name


class RutuGrain(models.Model):
    Name = models.ForeignKey(Rutu,on_delete = models.DO_NOTHING)
    grain = models.ForeignKey(grain, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.Name

class RutuNew(models.Model):
    Name = models.CharField(max_length=300)
    zone = models.ForeignKey(Zone,on_delete = models.DO_NOTHING)
    description = models.TextField(blank=True)
    fromDate = models.DateTimeField(default = datetime.now)
    toDate = models.DateTimeField(default = datetime.now)
    allowedDescr = models.TextField(blank=True)
    notAllowedDescr = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    
    grain = models.ManyToManyField(grain,related_name='grain' )
    spices = models.ManyToManyField(spices, related_name='spices')
    fruits = models.ManyToManyField(fruits, related_name='fruits')
    fruitJuices = models.ManyToManyField(fruitJuices, related_name='fruitJuices')
    vegetables = models.ManyToManyField(vegetables, related_name='vegetables')
    leafyveg = models.ManyToManyField(leafyveg, related_name='leafyveg')
    drinks = models.ManyToManyField(drinks, related_name='drinks')
    lentils = models.ManyToManyField(lentils, related_name='lentils')
    soup = models.ManyToManyField(soup, related_name='soup')
    nonVeg = models.ManyToManyField(nonVeg, related_name='nonVeg')
    legumes = models.ManyToManyField(legumes, related_name='legumes')

    def __str__(self):
        return self.Name