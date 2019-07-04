from django.shortcuts import render, HttpResponse, redirect
from random import randint
import datetime


def index(request):
    if 'gold' not in request.session:
        request.session["gold"] = 0
    if 'activites' not in request.session:
        request.session['activites'] = []

    return render(request,'ninja_gold/index.html')

def process_money(request):
    if request.POST['find'] == 'farm':
        number = randint(10,20)
        request.session['gold'] += number
        request.session['activites'].append("<p class='text-success'> Earned " + str(number) + " gold from farm! " + str(datetime.datetime.now()) + "</p>")

    if request.POST['find'] == 'cave':
        number = randint(5,10)
        request.session['gold'] += number 
        request.session['activites'].append("<p class='text-success'> Earned " + str(number) + " gold from cave! " + str(datetime.datetime.now()) + "</p>")

    if request.POST['find'] == 'house':
        number = randint(2,5)
        request.session['gold'] += number 
        request.session['activites'].append("<p class='text-success'> Earned " + str(number) + " gold from house! " + str(datetime.datetime.now()) + "</p>")

    if request.POST['find'] == 'casino':
        number = randint(-50,50)
        request.session['gold'] += number 
        if number >= 0:
            request.session['activites'].append("<p class='text-success'> Earned " + str(number) + " gold from casino! " + str(datetime.datetime.now()) + "</p>")
        else:
            request.session['activites'].append("<p class='text-danger'> Entered a casino and lost " + str(number) + " gold ... Ouch.. " + str(datetime.datetime.now()) + "</p>")


    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')