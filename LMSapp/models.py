import email
from django.db import models


class Book(models.Model):
    id = models.CharField(max_length= 10000, primary_key=True)
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000, blank=True)
    no_of_books_available = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


    
