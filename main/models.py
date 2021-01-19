from django.db import models

class BookStore(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    is_favorite = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)