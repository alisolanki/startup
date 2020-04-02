from django.db import models
from django.contrib.auth.models import User
from event.models import Event

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    img = models.ImageField(upload_to = 'pics/accounts', default = '../static/images/accounts/default-dp.png')
    name = models.CharField(max_length = 50)
    phonenumber = models.CharField(max_length = 13)

    def __str__(self):
        return self.user.username

class RegisteredEvent(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    eventid = models.CharField(max_length = 50)

    def __str__(self):
        return self.userprofile.name

