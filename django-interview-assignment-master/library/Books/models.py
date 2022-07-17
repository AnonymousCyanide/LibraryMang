from django.db import models
from django.contrib.auth.models import User
import datetime as DT
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length= 40 ,default='Unknown')
    price = models.FloatField(default= 5)

    def __str__(self):
        return self.title

class Borrowed(models.Model):
   
    STATUS = (
        ('Borrowed','Borrowed'),
        ('Returned','Returned'))
    borrowed_by = models.ForeignKey(User, on_delete= models.CASCADE)
    borrowed_book = models.OneToOneField(Book, on_delete=models.CASCADE)  #ForeignKey(Book, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.borrowed_by.username +'/' + self.borrowed_book.title
