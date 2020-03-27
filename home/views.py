from django.shortcuts import render
from event.models import Event

# Create your views here.
def home(request):
    
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})