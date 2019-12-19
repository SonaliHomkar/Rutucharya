from django.shortcuts import render
from datetime import datetime, timedelta
import calendar
from food.models import mealType, Menu
from django.contrib.auth.models import User
from .models import mealData
from django.core import serializers
from django.http import HttpResponse
 
def mealPlan(request):
    todayDate = datetime.now
    year, week, dow = datetime.today().isocalendar()
    Weekdata = []
    daycnt =0

    lstmealType = mealType.objects.all()
    print(lstmealType)

    for x in range(dow,8):
        actDate = (datetime.today()  + timedelta(days=daycnt)).strftime('%m-%d-%Y')
        startDate = (datetime.today()  + timedelta(days=daycnt)).strftime('%d  %b ,%Y %A')
        idict = {"startDate": startDate , "actDate" : actDate }
        Weekdata.append(idict)    
        daycnt += 1
    
    
    context = {
        'Weekdata'  : Weekdata,
        'lstmealType'   : lstmealType,        
    }
    return render(request, 'mealPlan/mealPlan.html', context)


def selectMenu(request,mealType,mealDate,actDate):
    lstMenu = Menu.objects.all()
    context = {
        'lstMenu'   :   lstMenu,
        'mealType'  :   mealType,
        'mealDate'  :   mealDate,
        'actDate'   :   actDate,
            
    }
    return render(request, 'mealPlan/selectMenu.html', context)

def saveMenu(request):
    if request.method == "POST":
        MenuId =  Menu.objects.get(id=request.POST['menulist']) 
        mType =  mealType.objects.get(id=int(request.POST['mealType'])) 
        
        mDate =  request.POST['actDate']
        mDate = datetime.strptime(mDate,'%m-%d-%Y')
        userId =  request.user.id 
        print('into saved : ' +  str(mType))
        print('mealDate : ' +  str(mDate))
        print('menu : ' + str(MenuId))
        print('userId : ' + str(request.user.id))


        objmealPlan = mealData(dateOfMeal = mDate , typeOfMeal = mType,
        menuId = MenuId,userId = userId )
        

        objmealPlan.save()

        
        context = {
            'saved' : 'saved'
        }
        return render(request,'mealPlan/mealPlan.html',context) 

def showMealPlan(request):
    objMealData = mealData.objects.all()
    context = {
            'objMealData' : objMealData
        }

    return render(request,'mealPlan/displayMealPlan.html',context)

def showMealPlanJson(request):
    objMealData = mealData.objects.all()
    objMealData_list = serializers.serialize('json',objMealData)
    return HttpResponse(objMealData_list,content_type= "text/json-comment-filtered")