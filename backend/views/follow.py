from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from backend.models import User, Post, Follower, Profile

@login_required
def follow(request):
    user_id = request.user.pk
    user = get_object_or_404(User, pk=user_id)
    if request.user != user:
        already_followed = Follower.objects.filter(user=user, is_followed_by=request.user).first()
        if not already_followed:
            new_follower = Follower(user=user, is_followed_by=request.user)
            new_follower.save()
            follower_count = Follower.objects.filter(user=user).count()
            return JsonResponse({'status':'Following', 'count':follower_count})
        else:
            already_followed.delete()
            follower_count = Follower.objects.filter(user=user).count()
            return JsonResponse({'status':'Not following', 'count':follower_count})
    return redirect('/')

@login_required
def following(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    following_list = Follower.objects.filter(is_followed_by=user)
    return render(request, 'social/following.html',{'theuser':user,'following_list':following_list})

@login_required
def followers(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    follower_list = Follower.objects.filter(user=user).exclude(is_followed_by=user)
    return render(request, 'social/followers.html',{'theuser':user,'followers_list':follower_list})