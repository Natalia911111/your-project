from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from users import forms
from django.contrib import messages
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect(reverse('home:home'))

def registration_view(request):
    form = forms.RegistrationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.ERROR, f'You are registered. Please login')
            return redirect(reverse('login'))
    return render(request,'users/registration.html', {'form': form})

def login_user_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(email=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, f'Congrats {username}')
                    return redirect(request.GET.get('next', reverse('home:home')))
    else:
        form = forms.LoginForm()
    return render(request, 'users/login.html', {'form': form})