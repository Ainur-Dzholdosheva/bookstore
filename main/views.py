from django.shortcuts import render, HttpResponse, redirect
from .models import BookStore

def homepage(request):
    book_store = BookStore.objects.all()
    return render(request, "book.html", {"book_store": book_store})

def add_book(request):
    form = request.POST
    text = form["book_text"]
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    price = form["book_price"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    book = BookStore(title=text, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book.save()
    return redirect(homepage)