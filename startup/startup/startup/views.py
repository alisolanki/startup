from django.shortcuts import render

# Create your views for startup here.
def index(request):
    return render(request, 'index.html', {})

def elements(request):
    return render(request, 'elements.html', {})