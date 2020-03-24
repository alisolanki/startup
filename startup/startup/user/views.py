from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create your views here.
def user(request, slug):
    user = User.objects.get(username = slug)
    userprofile = UserProfile.objects.get(user = user)
    return render(request, 'user.html', {'userprofile' : userprofile,'user': user})