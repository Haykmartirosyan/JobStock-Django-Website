from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = True
            user.save()

    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def signin(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("redirect any whre u want")

    return render(request, 'accounts/index.html')


def logout_user(request):
    user = request.user
    logout(request)
    return render(request, "accounts/index.html")