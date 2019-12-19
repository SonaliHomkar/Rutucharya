from django.db import models

from datetime import datetime
from food.models import mealType,Menu
from django.contrib.auth.models import User
from django.core import serializers


class mealData(models.Model):
    dateOfMeal = models.DateField(blank=True)
    typeOfMeal = models.ForeignKey(mealType, on_delete = models.DO_NOTHING)
    menuId = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    userId = models.IntegerField(blank=True)

    def __str__(self):
        return self.mealType.mealType
        return self.Menu.menuName
    

