from django.db import models

# Create your models here.
class Event:
    id: int
    img: str
    name: str
    date: str
    place: str
    time: str
    price: int