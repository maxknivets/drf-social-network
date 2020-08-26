from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from backend.models import User, Post, Follower, Profile
from backend.forms import Edit_form, Delete_form, Change_profile_info_form, Profile_picture_form
import datetime

@login_required
def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    users_posts = Post.objects.filter(user=user)
    return render(request, 'social/user.html', {
        'user_info': user,
        'request_user': request.user, 
        'latest_posts_list': users_posts, 
        'latest_post': users_posts,
        'editform':Edit_form(),
    })

@login_required
def changeinfo(request):
    changes_saved = None
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        changes_saved = False
        form = Change_profile_info_form(request.POST)
        profile_picture_form = Profile_picture_form(request.POST, request.FILES)
        if profile_picture_form.is_valid():
            changes_saved = True
            profile.profile_picture = profile_picture_form.cleaned_data['profile_picture']
            profile.save()
        elif form.is_valid():
            changes_saved = True
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()
            profile.bio = form.cleaned_data['bio']
            profile.location = form.cleaned_data['location']
            profile.save()
    form = Change_profile_info_form(initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'bio': profile.bio,
        'location': profile.location,
    })
    return render(request, 'social/change_info.html', {
        'change_profile_info_form': form, 
        'profile_picture_form': Profile_picture_form, 
        'response': changes_saved, 
        'logged_user': request.user.pk
    })