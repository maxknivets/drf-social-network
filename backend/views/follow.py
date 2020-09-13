from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse

from backend.models import User, Post, Follower, Profile
from backend.serializers import FollowerSerializer
from rest_framework import generics, mixins, permissions

@login_required
def follow(request, pk):
    user = get_object_or_404(User, pk = pk)
    already_followed = Follower.objects.filter(user = user, is_followed_by = request.user).first()
    if not already_followed:
        new_follower = Follower(user = user, is_followed_by = request.user)
        new_follower.save()
        follower_count = Follower.objects.filter(user = user).count()
        return JsonResponse({'status': 'Following', 'count': follower_count})
    else:
        already_followed.delete()
        follower_count = Follower.objects.filter(user = user).count()
        return JsonResponse({'status': 'Not following', 'count': follower_count})
    return redirect('/')

class Following(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = get_object_or_404(User, pk = self.kwargs["pk"])
        return Follower.objects.filter(is_followed_by = user)

class Followers(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = get_object_or_404(User, pk = self.kwargs["pk"])
        return Follower.objects.filter(user = user).exclude(is_followed_by = user)