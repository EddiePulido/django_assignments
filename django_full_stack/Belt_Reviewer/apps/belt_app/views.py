from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

from django.template.defaulttags import register

@register.filter
def hash(h, key):
    return h[key]


def index(request):
    if 'id' in request.session:
        return redirect("/books")
    return render(request,"belt_app/index.html")

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

# ★ ☆


def books(request):
    if 'id' not in request.session:
        return redirect("/")
    ratings = {
    '1': '<span class ="text-warning">★</span> ☆ ☆ ☆ ☆',
    '2': '<span class ="text-warning">★ ★</span> ☆ ☆ ☆',
    '3': '<span class ="text-warning">★ ★ ★</span> ☆ ☆',
    '4': '<span class ="text-warning">★ ★ ★ ★</span> ☆',
    '5': '<span class ="text-warning">★ ★ ★ ★ ★</span>'

    }
    context = {
        'books': Book.objects.all(),
        'reviews': Review.objects.all().order_by("-id")[:3],
        'ratings': {
            '1': '<span class ="text-warning">★</span> ☆ ☆ ☆ ☆',
            '2': '<span class ="text-warning">★ ★</span> ☆ ☆ ☆',
            '3': '<span class ="text-warning">★ ★ ★</span> ☆ ☆',
            '4': '<span class ="text-warning">★ ★ ★ ★</span> ☆',
            '5': '<span class ="text-warning">★ ★ ★ ★ ★</span>'

            }
    }
    
    return render(request,"belt_app/books.html",context)

def book_page(request,id):
    ratings = {
    '1': '<span class ="text-warning">★</span> ☆ ☆ ☆ ☆',
    '2': '<span class ="text-warning">★ ★</span> ☆ ☆ ☆',
    '3': '<span class ="text-warning">★ ★ ★</span> ☆ ☆',
    '4': '<span class ="text-warning">★ ★ ★ ★</span> ☆',
    '5': '<span class ="text-warning">★ ★ ★ ★ ★</span>'

    }
    context = {
        "book": Book.objects.get(id=id),
        'ratings' : ratings
    }
    
    return render(request,"belt_app/book_page.html",context)

def add_page(request):
    if 'id' not in request.session:
        return redirect("/")
    context = {
        "authors" : Author.objects.all()
    }

    return render(request,"belt_app/add_book.html",context)

def add_book(request):
    user = User.objects.get(id=request.session['id'])
    
    if request.POST['author_select'] == "None":
        author = Author.objects.get(name=request.POST['author'])
    else:
        author = Author.objects.create(name=request.POST['author_select'])

    book = Book. objects.create(title = request.POST['title'],author=author,uploader=user)

    review = Review.objects.create(review = request.POST['review'],rating = request.POST['rating'],book = book, reviewer = user)

    return redirect('/books/{}'.format(book.id))

def add_review(request):
    book = Book.objects.get(id=request.POST['book_id'])
    user = User.objects.get(id=request.session['id'])

    review = Review.objects.create(review=request.POST["review"], reviewer=user, rating=request.POST["rating"],book=book)

    return redirect("/books/{}".format(request.POST['book_id']))

def delete_review(request, id):
    review = Review.objects.get(id=id)
    review.delete()

    return redirect('/books')

def user_page(request,id):
    if 'id' not in request.session:
        return redirect("/")
    user = User.objects.get(id=id)
    reviews = user.reviews_posted.all().count()
    
    context = {
        'user': user,
        'reviews_count': reviews
    }
    return render(request, "belt_app/user_page.html",context)
















