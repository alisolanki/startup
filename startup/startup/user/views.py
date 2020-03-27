from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from accounts.models import UserProfile

# Create your views here.
def user(request, slug):
    user = User.objects.get(username=slug)
    userprofile = UserProfile.objects.get(user = user)
    if request.method == 'POST':
        # Profile Picture Update
        if 'picture' in request.FILES:
            
            img = request.FILES['picture']
            userprofile.img = img
            userprofile.save()
            return render(request, 'user.html', {'userprofile' : userprofile,'user': user})
        
        # Change data of the user
        else:
            # name = request.POST['name']
            # phonenumber = request.POST['phonenumber']
            # email = request.POST['email']
            # username = request.POST['username']
            # password1 = request.POST['password1']
            # password2 = request.POST['password2']
            # if password1==password2:
            #     if User.objects.filter(username=username).exists():
            #         messages.info(request,'Username already taken')
            #         return redirect('register')
            #     elif User.objects.filter(email=email).exists():
            #         messages.info(request,'Email already taken')
            #     else:    
            #         user = User.objects.create_user(username=username, password=password1, first_name=name, email=email)
            #         user = User.objects.get(username=username)
            #         profile = UserProfile(user=user, name=name, phonenumber=phonenumber)

            #         profile.save()
            #         user.save()
            return render(request, 'user.html', {'userprofile' : userprofile,'user': user})
    else:
        # user = User.objects.get(username = slug)
        # userprofile = UserProfile.objects.get(user = user)
        return render(request, 'user.html', {'userprofile' : userprofile,'user': user})