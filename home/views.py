from django.shortcuts import render
from event.models import Event
from place.models import Place

# Create your views here.
def home(request):
    
    events = Event.objects.all()
    places = Place.objects.all()
    return render(request, 'index.html', {'events': events, 'places': places})