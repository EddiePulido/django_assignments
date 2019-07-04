from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def random_word(request):
    rWord = get_random_string(14)

    dic = {
        'word' : rWord
    }
    if 'count' not in request.session:
        request.session['count'] = 1
    return render(request,"random_word/index.html", dic)

def generate(request):
    request.session['count'] += 1
    return redirect('/random_word') 

def reset(request):
    del request.session['count']
    return redirect('/random_word')