
# Create your views here.
# app/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# 1. Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('all_post')
        else:
            messages.success(request, 'Error logging in')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')

# 2. Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('login')

# 3. Registration View
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You are now registered and logged in')
            return redirect('all_post')
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/register.html', {'form': form})