"""
Definition of models.
"""

from django.db import models
class Users(models.Model):
    Id=models.IntegerField()
    UserName=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    Email=models.CharField(max_length=100)
    IsActive=models.BooleanField(default=true)

# Create your models here.
class UserSearch(models.Model):
    UserId=models.IntegerField()
    From_Town=models.CharField(max_length=20)
    To_Town=models.CharField(max_length=20)
    OneWay=models.BooleanField(default=False)
    adult=models.IntegerField()
    Child=models.IntegerField()
