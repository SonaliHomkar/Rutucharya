from django.urls import path
from  . import views

urlpatterns = [
    path('', views.mealPlan, name='mealPlan'),
    path('showMealPlan', views.showMealPlan, name='showMealPlan'),
    path('selectMenu/<str:mealType>/<str:mealDate>/<str:actDate>', views.selectMenu, name='selectMenu'),
    path('saveMenu', views.saveMenu, name='saveMenu'),
    path('showMealPlanjson', views.showMealPlanJson, name='showMealPlanjson')
    
]