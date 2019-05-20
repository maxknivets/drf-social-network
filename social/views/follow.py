from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from social.models import User, Post, Vote, Followers, Profile, Comment


def follow(request):
    user_id = request.GET.get('id')
    user = get_object_or_404(User, pk=user_id)
    if request.user.is_authenticated and request.user != user:
        already_followed = Followers.objects.filter(user=user, is_followed_by=request.user).first()
        if not already_followed:
            new_follower = Followers(user=user, is_followed_by=request.user)
            new_follower.save()
            followers_count = Followers.objects.filter(user=user).count()
            return JsonResponse({'status':'Following', 'count':followers_count})
        else:
            already_followed.delete()
            followers_count = Followers.objects.filter(user=user).count()
            return JsonResponse({'status':'Not following', 'count':followers_count})
    return redirect('/')


def following(request, user_id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=user_id)
        following_list = Followers.objects.filter(is_followed_by=user)
        return render(request, 'social/following.html',{'theuser':user,'following_list':following_list})
    return redirect('/')


def followers(request, user_id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=user_id)
        followers_list = Followers.objects.filter(user=user).exclude(is_followed_by=user)
        return render(request, 'social/followers.html',{'theuser':user,'followers_list':followers_list})
    return redirect('/')

