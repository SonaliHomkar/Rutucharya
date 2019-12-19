from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Rutu, RutuGrain, RutuNew

from food.models import foodType,food, grain


# Create your views here.
def rutu(request):
    rutuListing = RutuNew.objects.all()
    context = {
        'rutuListing' : rutuListing,
    }
    return render(request, 'rutu/rutu.html', context)

def rutuDetails(request):
    if request.method == "POST":
        chkGrains = request.POST.getlist('chkGrains')
        print(chkGrains)
        grainList = []
        
        for i in chkGrains:
            RutuName = request.POST['RutuName']
            print(RutuName)
            grainId = grain.objects.get(pk=i)
            RutuGrain.save(Name = RutuName, grain=grainId)
            grainList.append(grain.objects.get(pk=i))
    
        context = {
            'grainList' : grainList
        }
        return render(request,'rutu/rutudetails.html')

    else:
        grainsListing = grain.objects.all()
        rutuListing = Rutu.objects.all()
        context = {
            'rutuListing' : rutuListing,
            'grainsListing' : grainsListing,
        }
        return render(request, 'rutu/rutudetails.html', context)
    

def rutuNew(request):
    rutuListing = RutuNew.objects.all()
    grainsListing = grain.objects.all()
    context = {
        'rutuListing' : rutuListing,
        'grainsListing' : grainsListing,
    }
    return render(request, 'rutu/rutuNew.html', context)
    

def rutuIndividual(request,RutuId):
    rutulisting = get_object_or_404(RutuNew, pk = RutuId )
    context = {
        'rutulisting' : rutulisting,
    }
    return render(request, 'rutu/rutuIndividual.html', context)