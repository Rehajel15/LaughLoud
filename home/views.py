from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from .models import Joke, Notification, ReportedJoke
from authentication.models import Profile
from functools import wraps

def authorization():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, f"You need to sign in to have access to the home page.")
                return redirect('/authentication/')
            else:
                try:
                    profile = Profile.objects.get(username=request.user.username)
                    if profile.isBanned:
                        messages.error(request, "This account can no longer be used.")
                        logout(request)
                        return redirect('/authentication/signin/')
                except Profile.DoesNotExist:
                    pass
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator



def update_joke_categories():
    joke_categories = {
        'ShallowJokes': {
            'name': 'Shallow jokes',    
            'url': 'ShallowJokes',
            'table': Joke.objects.filter(category='Shallow jokes')
        },
        'DarkHumor': {
            'name': 'Dark humor',
            'url': 'DarkHumor',
            'table': Joke.objects.filter(category='Dark humor')
        },
        'LongJokes': {
            'name': 'Long jokes',
            'url': 'LongJokes',
            'table': Joke.objects.filter(category='Long jokes')
        },
        'CountryJokes': {
            'name': 'Country jokes',
            'url': 'CountryJokes',
            'table': Joke.objects.filter(category='Country jokes')
        },
        'FamilyFriendlyJokes': {
            'name': 'Family-friendly jokes',
            'url': 'FamilyFriendlyJokes',
            'table': Joke.objects.filter(category='Family-friendly jokes')
        }
    }
    return joke_categories


@authorization()
def main(request):
    if request.method == 'POST':
        joke_id = request.POST.get('joke_id')
        ReportCategory = request.POST.get('reportCategory')
        ReportTextField = request.POST.get('ReportTextField')
        joke = Joke.objects.get(id=joke_id).joke
        from_user = Joke.objects.get(id=joke_id).from_user

        if ReportTextField == '':
            ReportTextField = 'None'


        ReportedJoke.objects.create(joke_id=joke_id, ReportCategory=ReportCategory, ReportTextField=ReportTextField, joke=joke, from_user=from_user).save()
        messages.success(request, "Thank you for helping us keeping LaughLoud clean for everyone.")
        return redirect(request.path)
    return render(request, 'main.html', {'joke_categories': update_joke_categories})
    

@authorization()
def jokes(request, category):
    return render(request, category + '.html', {'joke_categories': update_joke_categories})


@authorization()
def upload(request):
    if request.method == 'POST':
        jokeInput = request.POST.get('joke')
        jokeCategory = request.POST.get('selected_category')
        from_user = request.user.username

        if len(jokeInput) > 100:
            messages.error(request, "Your joke is too long!")
            return render(request, 'upload.html', {'joke_categories': update_joke_categories, 'jokeInput': jokeInput, 'jokeCategory': jokeCategory})
        else:
            new_joke = Joke.objects.create(joke=jokeInput, category=jokeCategory, from_user=from_user)
            new_joke.save()
            messages.success(request, "Uploaded your joke successfully!")
        return redirect('/home/')
    
    return render(request, 'upload.html', {'joke_categories': update_joke_categories})
    

@authorization()
def rules(request):
    return render(request, 'rules.html')


@authorization()
def notifications(request):
    notifications = Notification.objects.filter(for_user__in=['', request.user.username],sended_on__gt=request.user.date_joined).order_by('-sended_on')
    return render(request, 'notifications.html', {'notifications': notifications})
    

@authorization()
def more(request):
    profile = {
        'username': request.user.username,
        'email_address': request.user.email,
        'password': request.user.password,
        'fname': request.user.first_name,
        'surname': request.user.last_name,
    }

    if request.method == 'POST':
        post = {
            'usernamePOST':  request.POST.get('profile_name'),
            'email_address':  request.POST.get('profile_email'),
            'fname':  request.POST.get('profile_firstname'),
            'password':  request.POST.get('profile_password'),
            'password_repeat':  request.POST.get('profile-repeat_password'),
            'surname':  request.POST.get('profile_surname'),
        }
        

        if post['password'] != post['password_repeat']:
            messages.error(request, "You repeated the wrong password!")
            return redirect('/home/settings')

        user = User.objects.get(username=request.user.username)

        user.username = post['usernamePOST']
        user.first_name = post['fname']
        user.last_name = post['surname']
        user.email = post['email_address']

        if post['password']:
            user.set_password(post['password'])

        user.save()
        logout(request)
        messages.success(request, "You have to sign in again for the changes to be saved.")
        return redirect('/authentication/signin')        

    return render(request, 'more.html', {'profile': profile})
    
    
