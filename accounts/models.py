from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    img = models.ImageField(upload_to = 'pics/accounts', default = '../static/images/accounts/default-dp.png')
    name = models.CharField(max_length = 50)
    phonenumber = models.CharField(max_length = 13)

    def __str__(self):
        return self.user.username

class RegisteredEvent(models.Model):
    registeredevent = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    eventid = models.IntegerField(default = -1)

    def __str__(self):
        return self.registeredevent.name

