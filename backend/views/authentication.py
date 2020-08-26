from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from backend.models import User
from rest_framework.authtoken.models import Token

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = Sign_up_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = Profile(user=user)
            profile.save()
            login(request, user)
            return redirect('/')
    else:
        form = Sign_up_form()
    return render(request, 'registration/signup.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('/login')

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

