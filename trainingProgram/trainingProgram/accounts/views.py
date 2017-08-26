from django.shortcuts import render
from battleships.forms import *
from battleships.models import GameUsers
from django.contrib.auth.models import User
from django.shortcuts import redirect
from trainingProgram.settings import LOGIN_REDIRECT_URL
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']

            GameUsers.firstname = firstname
            GameUsers.lastname = lastname
            GameUsers.username = username
            GameUsers.password = password1

            user = User.objects.create_user(username=username, email=email, password=password2)
            newUser = GameUsers(user=user, username=username, firstname=firstname, lastname=lastname, emailAdress=email)
            newUser.save()

            return redirect(LOGIN_REDIRECT_URL)
    else:
        form = registerForm()
    return render(request, "accounts/register.html", {'form': form})


def auth_login(request,template_name):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "main/home.html")
            else:
                print "bad login"
    else:
        form = loginForm()
    return render(request, "accounts/login.html", {'form': form})
