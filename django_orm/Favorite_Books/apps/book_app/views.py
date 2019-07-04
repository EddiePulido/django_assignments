from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    if 'id' in request.session:
        return redirect("/books")
    return render(request,"book_app/index.html")

def create(request):
    errors = User.objects.registration_validator(request.POST)

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        # redirect the user back to the form to fix the errors
        return redirect('/')

    hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=hash1)

    request.session['id'] = user.id
    request.session['first_name'] = user.first_name


    return redirect("/books")

def login(request):
    errors = User.objects.login_validator(request.POST)
    print(errors)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)

        return redirect("/")

    user = User.objects.get(email=request.POST['email'])
    request.session['id'] = user.id
    request.session['first_name'] = user.first_name



    return redirect("/books")



def logout(request):
    request.session.flush()

    return redirect("/")

def show_books(request):
    context={
        'books': Book.objects.all(),
        'user': User.objects.get(id=request.session['id'])
    }
    
    return render(request,"book_app/books.html",context)


def book_page(request,id):
    context = {
        'book': Book.objects.get(id=id),
        'this_user': User.objects.get(id=request.session['id'])
    }

    return render(request,"book_app/book_page.html",context)

def add_favorite(request,id):
    user = User.objects.get(id=request.session['id'])
    book = Book.objects.get(id=id)

    user.liked_books.add(book)

    return redirect("/books")

def add_book(request):
    user = User.objects.get(id=request.session['id'])
    book = Book.objects.create(title=request.POST['title'], desc=request.POST['description'], uploaded_by = user)
    user.liked_books.add(book)

    return redirect("/books")

def update(request):
    book = Book.objects.get(id=request.POST['book_id'])
    print(book.title)
    book.title = request.POST['title']
    print(book.title)
    book.desc = request.POST['description']
    book.save()

    return redirect("/books/{}".format(request.POST['book_id']))


def delete(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books')

def unfavorite(request,id):
    user = User.objects.get(id=request.session['id'])
    book = Book.objects.get(id=id)

    user.liked_books.remove(book)

    return redirect('/books/{}'.format(id))
























