from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def user(request, slug):
    user = User.objects.get(username = slug)
    return render(request, 'user.html', {'user': user})