from django.urls import path
from  . import views

urlpatterns = [
    path('', views.rutu, name='rutu'),
    path('rutudetails', views.rutuDetails, name='rutudetails'),
    path('rutuNew', views.rutuNew, name='rutuNew'),
    path('rutuIndividual/<int:RutuId>', views.rutuIndividual, name='rutuIndividual'),

]