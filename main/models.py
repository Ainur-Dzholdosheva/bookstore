from django.db import models

class BookStore(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    genre = models.BooleanField(default=False)
    author = models.CharField(max_length=20)
    year = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)