from django.db import models

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