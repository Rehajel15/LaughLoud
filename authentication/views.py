from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from home.models import Notification, Joke, ReportedJoke
from authentication.models import Profile
from home.views import update_joke_categories, authorization

# Create your views here.

def choose(request):
    return render(request, 'choose.html')


def SignIn(request):
    if request.user.is_authenticated:
        messages.error(request, f"You can't sign in because you already are. To do this please sign out.")
        return redirect('/authentication/')
    else:
        if request.method == 'POST':
            username = request.POST.get('profile_name')
            password = request.POST.get('profile_password')

            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, "Wrong username or password. Please try again.")
                return redirect('/authentication/signin/')
            
            AccBanned = Profile.objects.get(user=user).isBanned

            if AccBanned:
                messages.error(request, "This account can no longer be used.")
                return redirect('/authentication/signin/')
            else:
                login(request, user)
                return redirect('/home')
        return render(request, 'SignIn.html')


def SignUp(request):
    if request.user.is_authenticated:
        messages.error(request, f"You can't sign up because you are already signed in. To do this please sign out.")
        return redirect('/authentication/')
    else:
        if request.method == 'POST':
            email_address = request.POST.get('profile_email')
            username = request.POST.get('profile_name')
            password = request.POST.get('profile_password')
            password_repeat = request.POST.get('profile_password-repeat')
            fname = request.POST.get('profile_firstname')
            surname = request.POST.get('profile_surname')
            username_exists = User.objects.filter(username=username)
            usersWithEmail = User.objects.filter(email=email_address)
            
            profile = {
                'email_address': email_address,
                'username': username,
                'password': password,
                'password_repeat': password_repeat,
                'fname': fname,
                'surname': surname,
            }
            
        
            if usersWithEmail:
                for i in usersWithEmail:
                    if Profile.objects.filter(user=i, isBanned=True).exists():
                        messages.error(request, "This email address cannot be used to create accounts.")
                        return redirect('/authentication/signup')                
    
            if username_exists:
                print("Der Username exisitert")
                messages.error(request, f"Username '{username}' already exists! Please try another username.")
                return render(request, 'SignUp.html', {'profile': profile})
            
            elif password != password_repeat:
                messages.error(request, "You repeated the wrong password!")
                return render(request, 'SignUp.html', {'profile': profile})
            
            elif len(email_address) > 40:
                messages.error(request, "Too long email address! Please try one under 40 characters.")
                return render(request, 'SignUp.html', {'profile': profile})
            
            elif len(username) > 20:
                messages.error(request, "Too long username! Please try one under 20 characters.")
                return render(request, 'SignUp.html', {'profile': profile})
            
            elif len(fname) > 15:
                messages.error(request, "Too long first name! Please try to keep your first name under 15 characters.")
                return render(request, 'SignUp.html', {'profile': profile})

            elif len(surname) > 15:
                messages.error(request, "Too long surname! Please try to keep your surname under 15 characters.")
                return render(request, 'SignUp.html', {'profile': profile})

            else:
                myuser = User.objects.create_user(username, email_address, password)
                myuser.first_name = fname  # Setze den Wert für first_name
                myuser.last_name = surname
                myuser.save()
                Notification.objects.create(header = f'Welcome to LaughLoud {username}!', content = 'Thank you for creating an account. Now you are able to upload EVERY joke you know on this application. \nThe developer of LaughLoud wishes you a lot of fun!', for_user = username)
                Notification.objects.update()
                messages.success(request, "Your account has been successfully created.")

                return redirect('/authentication/signin/')
    return render(request, 'SignUp.html')

def SignOut(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('/authentication/signin')

@authorization()
def DeleteAccount(request):
    if request.method == 'POST':
        username = request.POST.get('profile_name')
        password = request.POST.get('profile_password')
        
        user = authenticate(username=username, password=password)
        if user and user==request.user:
            Joke.objects.filter(from_user = request.user.username).delete()
            ReportedJoke.objects.filter(from_user = request.user.username).delete()
            Notification.objects.filter(for_user=request.user.username).delete()
            update_joke_categories()
            logout(request)
            user.delete()
            messages.success(request, "Deleted account successfully.")
            return redirect('/authentication/')
        else:
            messages.error(request, "You entered the wrong username or password. Please try again.")
            redirect('/authentication/signin/')
    return render(request, 'DeleteAccount.html')
        

