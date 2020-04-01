from django.contrib import admin
from .models import UserProfile, RegisteredEvent

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(RegisteredEvent)