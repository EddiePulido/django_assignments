from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        "books_list": Book.objects.all()
    }

    return render(request,"book_app/index.html",context)
def authors(request):
    context = {
        "author_list": Author.objects.all()
    }

    return render(request,"book_app/authors.html",context)

def book_page(request,id):
    b = Book.objects.get(id=id)
    context = {
        "book" : b,
        "author_list" : Author.objects.exclude(books=b)
    }

    return render(request,"book_app/book_page.html", context)

def add_author_to_book(request):
    author = Author.objects.get(id=request.POST['author_id'])
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)

    return redirect("/books/{}".format(request.POST['book_id']))

def author_page(request,id):
    a = Author.objects.get(id=id)
    context = {
        "author" : a,
        "book_list" : Book.objects.exclude(authors=a)
    }

    return render(request,"book_app/author_page.html",context)

def add_book(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['description'])

    return redirect('/')

def add_author(request):
    Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])

    return redirect('/authors')

def add_book_to_author(request):
    author = Author.objects.get(id=request.POST['author_id'])
    book = Book.objects.get(id=request.POST['book_id'])
    book.authors.add(author)

    return redirect("/authors/{}".format(request.POST['author_id']))
