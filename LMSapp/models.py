from django.db import models

# Create Book Model i.e. Creating Book table in Database with columns - id, title, author, no_of_available_books
class Book(models.Model):
    id = models.CharField(max_length= 10000, primary_key=True)
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000, blank=True)
    no_of_books_available = models.CharField(max_length=1000, blank=True)

    # To be able to see title of the book in database
    def __str__(self):
        return self.title


    
