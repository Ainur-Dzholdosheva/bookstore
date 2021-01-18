from django.shortcuts import render, HttpResponse, redirect
from .models import BookStore

def homepage(request):
    book_store = BookStore.objects.all()
    return render(request, "book.html", {"book_store": book_store})

def add_book(request):
    form = request.POST
    text = form["book_text"]
    book = BookStore(title=text)
    book.save()
    return redirect(homepage)