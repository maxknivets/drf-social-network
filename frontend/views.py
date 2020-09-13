from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url="/login/", redirect_field_name=None)
def home(request):
    return render(request, 'frontend/app.html', {})
    
@login_required(login_url="/login/", redirect_field_name=None)
def comments_page(request, id):
    return render(request, 'frontend/app.html', {})

@login_required(login_url="/login/", redirect_field_name=None)
def profile_page(request, id):
    return render(request, 'frontend/app.html', {})

@login_required(login_url="/login/", redirect_field_name=None)
def settings_page(request):
    return render(request, 'frontend/app.html', {})

@login_required(login_url="/login/", redirect_field_name=None)
def followers_page(request, id):
    return render(request, 'frontend/app.html', {})

@login_required(login_url="/login/", redirect_field_name=None)
def following_page(request, id):
    return render(request, 'frontend/app.html', {})