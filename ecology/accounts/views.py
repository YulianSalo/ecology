from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView as login
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm

@login_required()
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            userClass = form.cleaned_data.get('userClass')
            userLogin = form.cleaned_data.get('userLogin')
            userEmail = form,cleaned_data.get('userEmail')
            raw_password = form.cleaned_data.get('userPassword')
            user = authenticate(username=user.userLogin, password=raw_password)
            login(request, user)
            return redirect('eco:home')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})