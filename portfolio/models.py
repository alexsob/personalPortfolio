from email.mime import image
from pickle import TRUE
from turtle import title
from django.db import models

class Project(models.Model):
     title = models.CharField(max_length=100)
     description = models.CharField(max_length=250)
     image = models.ImageField(upload_to='portfolio/images/')
     url = models.URLField(blank=TRUE)

     def __str__ (self):
          return self.title
     