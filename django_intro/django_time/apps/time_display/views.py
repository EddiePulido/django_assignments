from django.shortcuts import render, redirect
from time import gmtime, strftime, localtime
    
def index(request):
    context = {
        # "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%I:%M %p",localtime())
    }
    return render(request,'time_display/index.html', context)

def time_display(request):
    return redirect('/')