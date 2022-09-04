from unicodedata import name
from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return f'{self.name}'



class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.CharField(max_length=200, default='Uncategorized')
    created = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return f'{self.title} | {self.author}'