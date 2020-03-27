"""User Views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

# Local
from users.models import Profile


def login_view(request):
    """Login view"""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        
            return redirect('feed')

        else:
            return render(request, 'users/login.html', {'error': 'Invalid User'})

    return render(request, 'users/login.html')


def signup_view(request):
    """Sign up view"""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if password != passwd_confirmation:
            return render(request, "users/signup.html", {'error' : 'Passwords does not match'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, "users/signup.html", {'error' : 'User already in use, try with other.'})

        user.email = request.POST['email']
        user.last_name = request.POST['last_name']
        user.first_name = request.POST['first_name']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')


    return render(request, "users/signup.html")

def update_profile(request):
    """Update Profile"""

    profile = request.user.profile

    return render(
        request=request,
        template_name="users/update_profile.html",
        context={
            'profile' : profile,
            'user' : request.user
        }
        )


@login_required
def logout_view(request):
    """Logout View"""

    logout(request)

    return redirect('login')

