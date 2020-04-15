from django.shortcuts import render
from event.models import Event
from .models import Place
# Create your views here.
def place(request):
    events = Event.objects.all()
    return render(request, 'place.html', {'events': events})

def placeid(request, place):
    placeid = Place.objects.get(name = place)
    places = Event.objects.filter(place = placeid)
    return render(request, 'place.html', {'place': place,'places': places})