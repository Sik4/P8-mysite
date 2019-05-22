from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                User.objects.get(email=form.cleaned_data.get("email"))
                
            except User.DoesNotExist:
                user = form.save()
                # Normalising data for username
                username = form.cleaned_data.get('username')
                messages.success(request, f'New Account Created:{username}')

                login(request, user)
                messages.info(request, f'You are now logged in as {username}')

                return redirect("index:homepage")
            else:
                messages.error(request, 'Email already used')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = UserRegisterForm
    return render(request, 'users/register.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("index:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged n as {username}")
                return redirect("index:homepage")
            else:
                messages.error(request, "Invalid username or password")
    else:
        messages.error(request, "Are you sure this is Username and Password ? ")

    form = AuthenticationForm(request.POST)
    return render(request,
                  "users/login.html",
                  {"form": form})
