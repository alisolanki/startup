from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length = 50)
    phonenumber = models.CharField(max_length = 13)

    def __str__(self):
        return self.user.username
    
