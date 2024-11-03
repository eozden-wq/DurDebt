from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255, default='')
    first_name= models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    balance = models.FloatField(default=0)
    
    def __str__(self):
        return self.first_name