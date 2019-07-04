from django.shortcuts import render

def index(request):

    return render(request,"poke_app/index.html")