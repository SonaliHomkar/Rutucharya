from django.urls import path
from  . import views


# create your views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),

]