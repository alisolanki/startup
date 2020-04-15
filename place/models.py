from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Place(models.Model):
    img = models.ImageField(upload_to = 'pics/place')
    name = models.CharField(max_length = 50, default = 'place-name')

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Place)
def submission_delete(sender, instance, **kwargs):
    instance.img.delete(False)