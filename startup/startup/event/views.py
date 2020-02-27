from django.shortcuts import render
from .models import Event

# Create your views here.
def event(request):
    event1 = Event()
    event1.name = "Model's Night"
    event1.place = "Play The Lounge"
    event1.img = 'image-1.jpg'

    event2 = Event()
    event2.name = "Gentlemen's Night"
    event2.place = "Some Place"
    event2.img = 'image-2.jpg'

    events = [event1, event2]
    return render(request, 'event.html', {'events': events})