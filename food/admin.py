from django.contrib import admin
from .models import food, mealType, Menu, foodType, Excercise, grain, legumes
from .models import vegetables, leafyveg, lentils, fruits, fruitJuices, drinks, nonVeg, soup, spices

# Register your models here.
admin.site.register(food)
admin.site.register(mealType)
admin.site.register(Menu)
admin.site.register(foodType)
admin.site.register(Excercise)
admin.site.register(grain)
admin.site.register(vegetables)
admin.site.register(leafyveg)
admin.site.register(lentils)
admin.site.register(fruits)
admin.site.register(fruitJuices)
admin.site.register(drinks)
admin.site.register(nonVeg)
admin.site.register(soup)
admin.site.register(spices)
admin.site.register(legumes)

