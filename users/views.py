from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Normalising data for username
            username = form.cleaned_data.get('username')
            messages.success(request, f'New Account Created:{username}')

            login(request, user)
            messages.info(request, f'You are now logged in as {username}')

            return redirect("index:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = UserRegisterForm
    return render(request, 'users/register.html', {'form': form})


"""
    form = UserRegisterForm

    return render(request=request,
                  template_name="index/register.html",
                  context={"form": form})
"""
