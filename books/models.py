from django.db import models

class Book(models.Model):
    title = models.CharField( max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13) #13 digit ISBN -> Unique book identifier of published book
    
    def __str__(self):
        return self.title