from django.db import models

# Create your models here.
class foodType(models.Model):
    foodType = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.foodType

class food(models.Model):
    Name = models.CharField(max_length=200)
    foodType = models.ForeignKey(foodType, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.Name

class mealType(models.Model):
    mealType = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.mealType
    
    class Meta:
        unique_together = ['mealType']

class Menu(models.Model):
    menuName = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    mealType = models.ForeignKey(mealType,on_delete=models.DO_NOTHING)
    ingredients = models.TextField()
    recipie = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.menuName
        
    class Meta:
        unique_together = ['menuName']

    
class Excercise(models.Model):
    excercise = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.excercise

class grain(models.Model):
    grainName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.grainName
    
    @property
    def serialize(self):
        return{
            'id':   self.id,
            'grainName':   self.grainName,
            'photo_main': self.photo_main
            }


class vegetables(models.Model):
    vegName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.vegName
    
class leafyveg(models.Model):
    leafyVegName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.leafyVegName

class lentils(models.Model):
    lentilName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.lentilName

class fruits(models.Model):
    fruitName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.fruitName

class fruitJuices(models.Model):
    fruitJuiceName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.fruitJuiceName


class drinks(models.Model):
    drinkName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.drinkName


class nonVeg(models.Model):
    nonVegName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.nonVegName

class soup(models.Model):
    soupName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.soupName

class spices(models.Model):
    spiceName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.spiceName

class legumes(models.Model):
    legumesName = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.legumesName



