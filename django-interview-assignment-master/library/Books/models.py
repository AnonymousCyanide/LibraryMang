from django.db import models

# Create your models here.

class Book(models.Model):
    status_choices = (('Borrowed','Borrowed'),('Available','Available'))
    title = models.CharField(max_length= 40 ,default='Unknown')
    status = models.CharField(max_length=10, choices= status_choices , default='Available')
    borrowed_till = models.DateField(null=True , blank=True)
    
