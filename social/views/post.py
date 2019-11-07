from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.utils.html import escape
from social.models import User, Post, Vote
from social.serializers import PostSerializer, PostListSerializer, PostEditSerializer
from rest_framework import generics, viewsets
from rest_framework.response import Response
    
class RetrievePosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    
class WritePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    

class VoteOnPost(generics.GenericAPIView):
    queryset = Vote.objects.all()
        
    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        post = get_object_or_404(Post, pk=request.POST.get('post_id'))
        vote = request.POST.get('vote')
        already_voted = queryset.filter(voted_by=request.user, voted_post=post).first()
        if already_voted:
            if already_voted.vote == 'L' and vote != 'L':
                already_voted.vote = 'D'
                already_voted.save()
            elif already_voted.vote == 'D' and vote != 'D':
                already_voted.vote = 'L'
                already_voted.save()
            else:
                already_voted.delete()
        else:
            already_voted = Vote(voted_post=post, voted_by=request.user, vote=vote)
            already_voted.save()
        likes = Vote.objects.filter(vote='L', voted_post=post).count()
        dislikes = Vote.objects.filter(vote='D', voted_post=post).count()
        data = {'total_likes':likes, 'total_dislikes':dislikes}
        return Response(data)


class Edit(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostEditSerializer
    
def delete(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        if request.user == post.user:
            post.delete()
    return redirect('/')

