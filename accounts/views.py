from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserProfile, RegisteredEvent
from event.models import NewUserRegisterEvent

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    else:
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
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
            else:    
                user = User.objects.create_user(username=username, password=password1, first_name=name, email=email)
                user = User.objects.get(username=username)
                profile = UserProfile(user=user, name=name, phonenumber=phonenumber)

                profile.save()
                user.save()

                return redirect('login')
            return redirect('register')
        else:
            messages.info(request,'Passwords not matching')
            return redirect('register')
    else:
        return render(request, 'register.html', {})

def logout(request):
    auth.logout(request)
    return redirect('/')

def registerevent(request):
    if request.method == 'POST':
        name = request.POST['name']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        people = request.POST['people']
        slug = request.POST['slug']

        if request.user.is_authenticated:
            user = User.objects.get(username = request.user.username)
            userprofile = UserProfile.objects.get(user = user)
            username = request.POST['username']

            registeredevent = RegisteredEvent(userprofile = userprofile, eventid = slug, name = name, email = email, phonenumber = phonenumber, number_of_people = people, username = username)
            registeredevent.save()

            return redirect('/')
        else:
            registeredevent = NewUserRegisterEvent(eventid = slug, name = name, email = email, phonenumber = phonenumber, number_of_people = people)
            registeredevent.save()

            return redirect('/')