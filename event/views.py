from django.shortcuts import render
from .models import Event
from accounts.models import RegisteredEvent
from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create your views here.
def event(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})

def eventid(request, slug):
    events = Event.objects.all()
    eventid = Event.objects.get(slug = slug)
    user = User.objects.get(username = request.user.username)
    userprofile = UserProfile.objects.get(user = user)
    registeredevent = RegisteredEvent.objects.filter(userprofile = userprofile, eventid = slug).first() # There is only one object
    return render(request, 'event.html', {'eventid': eventid, 'events': events, 'registeredevent': registeredevent, 'slug': slug})