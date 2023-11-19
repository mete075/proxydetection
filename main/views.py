from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, "main/home.html")

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account is gemaakt")


            return redirect('login')

    context = {'form':form}
    return render(request, "main/register.html", context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Gebruikersnaam of Wachtwoord is fout')
            return render(request, "main/login.html")
        

    return render(request, "main/login.html")


def logoutUser(request):
    logout(request)
    return redirect('home')

