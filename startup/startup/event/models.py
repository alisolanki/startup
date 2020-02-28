from django.db import models

# Create your models here.
class Event(models.Model):
    img = models.ImageField(upload_to = 'pics')
    name = models.CharField(max_length = 50)
    date = models.DateField()
    place = models.CharField(max_length = 50)
    time = models.TimeField()
    price = models.IntegerField(default=0)