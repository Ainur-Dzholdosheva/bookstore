from django.shortcuts import render, HttpResponse
from .models import BookStore

def homepage(request):
    book_store = BookStore.objects.all()
    return render(request, "book.html", {"book_store": book_store})
