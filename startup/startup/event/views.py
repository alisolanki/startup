from django.shortcuts import render
from .models import Event

# Create your views here.
def event(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})

def eventid(request, slug):
    events = Event.objects.all()
    eventid = Event.objects.get(slug = slug)
    return render(request, 'event.html', {'eventid': eventid, 'events': events})