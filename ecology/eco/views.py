from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from eco.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            raw_password = form.cleaned_data.get('userPassword')
            user = authenticate(username=user.userLogin, password=raw_password)
            login(request, user)
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})