from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserProfile

# Create your views here.
def login(request):
    return render(request, 'login.html', {})

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
            else:    
                user = User.objects.create_user(username=username, password=password1, first_name=name, email=email)
                user = User.objects.get(username=username)
                profile = UserProfile(user=user, name=name, phonenumber=phonenumber)

                profile.save()
                user.save()

                return redirect('/register/')
            return redirect('/')
        else:
            messages.info(request,'Passwords not matching')
    else:
        return render(request, 'register.html', {})