from django.db import models
from django.db.models.signals import post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Event(models.Model):

    img = models.ImageField(upload_to = 'pics')
    name = models.CharField(max_length = 50, default = 'event-name')
    slug = models.CharField(max_length = 50, default = 'name%place%01%01%2001%')
    date = models.DateField()
    place = models.CharField(max_length = 50)
    time = models.TimeField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Event)
def submission_delete(sender, instance, **kwargs):
    instance.img.delete(False)

class NewUserRegisterEvent(models.Model):

    name = models.CharField(max_length = 50, default = 'name')
    eventid = models.CharField(max_length = 50, default = "null")
    email = models.EmailField(max_length = 254, default = "null")
    phonenumber = models.CharField(max_length = 13, default = 0)
    number_of_people = models.IntegerField(default = 0)

    def __str__(self):
        return self.phonenumber