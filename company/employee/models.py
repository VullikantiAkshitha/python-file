# employee/models.py
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    joining_date = models.DateField()

    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    
