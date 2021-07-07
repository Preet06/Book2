from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
   Book_Name = models.CharField(max_length=200)
   Author = models.CharField(max_length=200)
   Genre  = models.CharField(max_length=200)
   Language = models.CharField(max_length=200)


   def __str__(self):
      return self.Book_Name

   def get_absolute_url(self):
       return reverse('home_page')