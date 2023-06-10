from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'members/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'members/login.html', context)

