from django.db import models

class BookStore(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.BooleanField(default=False)
    price = models.BooleanField(default=False)
    genre = models.BooleanField(default=False)
    author = models.BooleanField(default=False)
    year = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)