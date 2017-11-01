from django.shortcuts import render, HttpResponse, redirect
from random import randint
import random
# Create your views here.

def index(request):
    if 'totalGold' not in request.session:
        request.session['totalGold']=0


    return render(request, 'my_app/index.html')

def processMoney(request):
    if request.method == 'POST':
        location = request.POST['numGold']
        request.session['location']=location
        if 'farmGold' == location:
            request.session['totalGold'] += random.randint(100,300)
            print '----'
        if 'caveGold' == location:
            request.session['totalGold'] += random.randint(5,10)
            print '*********'            
        if 'houseGold' == location:
            request.session['totalGold'] += random.randint(2,5)
            print '----******-----'
        if 'casinoGold' == location:
            request.session['totalGold'] += random.randint(-50,50)

            print '***********'
  
  
        # request.session['newGold']= request.POST['numGold']

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')