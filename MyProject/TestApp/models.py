from django.db import models
from django.utils import timezone 

# Create your models here.

class App(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField() 
    pub_date = models.DateField(default=timezone.now())

    objects = models.Manager()

    def __str__(self):
        return self.author

class App2(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField() 

class RegistrationData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)