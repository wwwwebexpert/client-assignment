from django.db import models

# Create your models here.

class Client(models.Model):  
    cusername = models.CharField(max_length=100, unique=True)
    cname = models.CharField(max_length=255, blank=True)  
    cemail = models.EmailField()  
    cphone = models.CharField(max_length=15)  
    cstreet = models.CharField(max_length=255, blank=True)  
    csuburb = models.CharField(max_length=100, blank=True)  
    cpostcode = models.CharField(max_length=15, blank=True)  
    cstate = models.CharField(max_length=100, blank=True)  