from django.contrib import admin
from .models import Event, NewUserRegisterEvent

# Register your models here.

admin.site.register(Event)
admin.site.register(NewUserRegisterEvent)
