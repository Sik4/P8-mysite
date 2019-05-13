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
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, 'Votre compte a bien été crée')
            return redirect("index:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserRegisterForm()
    return render(request,
                  "index/register.html",
                  context={"form":form})

