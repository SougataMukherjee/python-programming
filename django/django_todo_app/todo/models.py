from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Todo(models.Model):
       task = models.CharField(max_length=200)
       completed = models.BooleanField(default=False)
       # you can use models.IntegerField() 

       def __str__(self):
           return self.task