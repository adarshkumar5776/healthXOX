from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from dietChart.models import info
from dietChart.models import diet
from dietChart.models import diet1
from dietChart.models import FoodTracker
theList1=[]
theList2=[]
theList3=[]

# Create your views here.
def home1(request):
  return render(request,'index.html')
def dietChart(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        weight=request.POST['weight']
        height=request.POST['height']
        gender=request.POST['gender']
        lmg=request.POST['LossGain']
        goal=request.POST.get('goal',False)
        active=request.POST["active"]
        height=int(height)
        age=int(age)
        weight=int(weight)
        goal=int(goal)
        w=abs(weight-goal)
        if age>=1 and age<=3:
         protien=13+weight
         fat=weight+w+5
         carbs=weight*5+w+5
        elif age>=4 and age<=8:
         protien=19+weight
         fat=weight+w+10
         carbs=weight*5+w+10
        elif age>=9 and age<=13:
         protien=34+weight
         fat=weight+w+10
         carbs=weight*5+w+10
        elif age>=14 and age<=18:
         protien=46+weight
         fat=weight+w+10
         carbs=weight*5+w+10
        elif age>=19 and age<=70:
         protien=52+weight
         fat=weight+w+15
         carbs=weight*5+w+15
        if height>140 and height<=150:
         protien= protien+5
        elif height>150 and height<=160:
          protien= protien+10   
        elif height>160 and height<=170:
              protien= protien+20
        elif height>170 and height<=180:
              protien= protien+25
        elif height>180:
              protien= protien+30     

        
        saverecord=info(name=name,age=age,height=height,weight=weight,gender=gender,lmg=lmg,goal=goal,active=active,protien=protien,fat=fat,carbs=carbs)
        saverecord.save()
        return redirect('/')
    data=info.objects.all()
    count =info.objects.count()
    if(count>0):
     data1=info.objects.get()
     lmg1=data1.lmg
    
     a=False
     if lmg1=='Gain Weight':
        a=True
     return render(request,'newform.html',{'data':data,'count':count,'lmg1':lmg1,a:'a'})
    return render(request,'newform.html',{'data':data,'count':count})
    

def diets(request):
  data=diet.objects.all()
  
  
  return render(request,'diet.html',{'data':data})
  
def diets1(request):
    data=diet1.objects.all()
  
  
    return render(request,'diet.html',{'data':data})

def foodTrack(request):
    P=0
    C=0
    F=0
    if request.method=='POST':
        food=request.POST['food']
        data=FoodTracker.objects.get(Foods=food)
        theList1.append(data.Protien)
        theList2.append(data.Fat)
        theList3.append(data.Carbs)
       
        for ele1 in range(0, len(theList1)):
          P = P + theList1[ele1]
        for ele2 in range(0, len(theList2)):
              F = F + theList2[ele2]
        for ele3 in range(0, len(theList3)):
              C = C + theList3[ele3]
    records1=info.objects.all()
    records=FoodTracker.objects.all()
    return render(request,'food_tracker.html',{'records':records,'records1':records1,'P':P,'C':C,'F':F,"dif" : (records1[0].protien - P) , "dif1" : (records1[0].fat - F) , "dif2" : (records1[0].carbs - C)})
 