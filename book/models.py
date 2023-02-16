from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=225,blank=False, null=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=False, blank=False, related_name='author_book')

    def __str__(self):
        return self.name    
    def get_absolute_url(self):
        # return reverse('books')
        pass


class Author(models.Model):
    name = models.CharField(max_length=225, blank=False, null=False)

    def get_absolute_url(self):
        ''' return url to redirect the user after CreateAuth'''
        return reverse('books:author_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
