from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt
from .forms import PostForm

def index(request):
  """
  Fetch all posts and render full index page with form
  """
  

  context = {
      'posts': Post.objects.all(),
      'new_post_form' : PostForm()

  }
  return render(request, 'ajax_app/index.html', context)


def post(request):

    if request.method == 'POST':
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            Post.objects.create(post=request.POST['post'])


    context = {
        'posts' : Post.objects.all()
    }

    return render(request, 'ajax_app/post_index.html',context)
