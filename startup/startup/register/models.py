from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class register(models.Model):
    person_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.person_name

class details(models.Model):
    register = models.ForeignKey(register, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
        
    def __str__(self):
        return self.phone_number