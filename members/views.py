from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/overview')
    else:
        form = CreateUserForm
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'members/register.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('/overview')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/overview')
            else:
                messages.info(request, "Username OR password is incorrect")

        context = {}
        return render(request, 'members/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

