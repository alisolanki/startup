from django.shortcuts import render
from event.models import Event

# Create your views here.
def place(request):
    events = Event.objects.all()
    return render(request, 'place.html', {'events': events})

def placeid(request, place):
    place = place
    placeid = Event.objects.filter(place = place)
    places = Event.objects.filter(place = place)
    return render(request, 'place.html', {'place': place, 'placeid': placeid,'places': places})