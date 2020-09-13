from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from backend.models import User, Post, PostRate
from backend.serializers import PostSerializer, PostRateSerializer
from backend.permissions import IsPostOwner

from rest_framework import generics, viewsets, mixins, permissions
from rest_framework.decorators import action

class PostViewSet(viewsets.ModelViewSet):
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsPostOwner]

    @action(detail=False, methods=['GET'], name='Get comments')
    def list_comments(self, request, *args, **kwargs):
        queryset = Post.objects.filter(in_reply_to_post = self.kwargs["pk"])
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def get_queryset(self):
        if self.action == 'list':
            return Post.objects.filter(in_reply_to_post = None).order_by('-pub_date')
        return Post.objects.order_by('-pub_date')

class PostRateViewSet(generics.GenericAPIView): # use mixins instead
    queryset = PostRate.objects.all()
    serializer_class = PostRateSerializer

    def get(self, request, pk):
        post = get_object_or_404(Post, pk = pk)
        data = {
            'likes_count': PostRate.objects.filter(liked = True, rated_post = post).count(), 
            'dislikes_count': PostRate.objects.filter(liked = False, rated_post = post).count()
        }
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk = request.data["rated_post"]["id"])
        post_rating = PostRate.objects.filter(rated_by = request.user, rated_post = post).first()
        user_liked_post = request.data["liked"]

        if post_rating:
            if user_liked_post:
                if post_rating.liked:
                    post_rating.liked = None
                else:
                    post_rating.liked = True                    
            elif not user_liked_post:
                if post_rating.liked == False:
                    post_rating.liked = None
                else:
                    post_rating.liked = False                    
        else:
            post_rating = PostRate(liked = user_liked_post, rated_by = request.user, rated_post = post)

        post_rating.save()

        data = {
            'total_likes': PostRate.objects.filter(liked = True, rated_post = post).count(), 
            'total_dislikes': PostRate.objects.filter(liked = False, rated_post = post).count()
        }
        return JsonResponse(data)

class CommentList(generics.ListAPIView): # turn this into a method in postviewset
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return Post.objects.filter(in_reply_to_post = self.kwargs["pk"])