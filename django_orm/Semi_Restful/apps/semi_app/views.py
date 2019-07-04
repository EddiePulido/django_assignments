from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import * 


def index(request):
    return redirect("/")

def shows(request):
    context = {
        'show_list' : Show.objects.all()
    }

    return render(request,"semi_app/index.html", context)

def add_page(request):
    return render(request,"semi_app/add_page.html")

def add(request):
    errors = Show.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:

        if Network.objects.filter(name=request.POST['network']).count() == 0:
            a = Network.objects.create(name=request.POST['network'])
        else:
            a = Network.objects.get(name=request.POST['network'])


        s = Show.objects.create(title=request.POST['title'],release_date=request.POST['date'],desc=request.POST['description'],network=a)
        return redirect('/shows/{}'.format(s.id))


def info(request,id):
    s = Show.objects.get(id=id)
    context = {
        "show": s
    }


    return render(request,"semi_app/show_page.html",context)

def edit_page(request,id):
    s = Show.objects.get(id=id)
    context = {
        "show" : s
    }

    return render(request,"semi_app/edit_page.html",context)

def edit(request,id):
    errors = Show.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/{}/edit'.format(id))
    else:

        if Network.objects.filter(name=request.POST['network']).count() == 0:
            a = Network.objects.create(name=request.POST['network'])
        else:
            a = Network.objects.get(name=request.POST['network'])

        s = Show.objects.get(id=id)
        s.title = request.POST['title']
        s.network = a
        s.release_date = request.POST['date']
        s.desc = request.POST['description']
        s.save()
        return redirect("/shows/{}".format(id))

def destroy(request,id):
    s = Show.objects.get(id=id)
    s.delete()

    return redirect("/shows")








