from unicodedata import category
from django.db import models
import datetime

# Create your models here.

class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  username = models.CharField(max_length=15)
  email = models.CharField(max_length=30)
  password = models.CharField(max_length=30)
  created = models.DateField(default= datetime.date.today)

class ToDo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=30)
  category = models.CharField(max_length=30)
  due_date = models.DateField(blank=True, null=True)
  description = models.TextField(blank=True)
  completed = models.BooleanField(default=False)
  created = models.DateField(default= datetime.date.today)
  updated = models.DateField(auto_now=True)
  

