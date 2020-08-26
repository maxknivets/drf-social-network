from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone

from backend.models import User, Post, PostRate
from backend.serializers import PostListSerializer, PostSerializer, PostRateSerializer

from rest_framework import generics, viewsets, mixins, generics
from rest_framework.views import APIView

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(in_reply_to_post=None)

class CommentList(generics.ListAPIView):
    serializer_class = PostListSerializer
    
    def get_queryset(self):
        return Post.objects.filter(in_reply_to_post=self.kwargs["pk"])

class CommentCount(APIView):

    def get(self, request, pk):
        comment_count = Post.objects.filter(in_reply_to_post=pk).count()
        return JsonResponse({'comment_count': comment_count})

class PostGet(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class PostDetail(mixins.CreateModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.data["posted_by"] = self.request.user.pk
        return self.create(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs):
        #check whether the user in post is the same as in request
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        #check whether the user in post is the same as in request
        return self.destroy(request, *args, **kwargs)

class PostRating(APIView):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        data = {
            'total_likes': PostRate.objects.filter(liked=True, rated_post=post).count(),
            'total_dislikes': PostRate.objects.filter(liked=False, rated_post=post).count()
        }
        return JsonResponse(data)

class RatePost(generics.GenericAPIView):
    queryset = PostRate.objects.all()
    serializer_class = PostRateSerializer

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=request.data["rated_post"]["id"])
        post_rating = PostRate.objects.filter(rated_by=request.user, rated_post=post).first()
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
            post_rating = PostRate(liked=user_liked_post, rated_by=request.user, rated_post=post)

        post_rating.save()

        data = {
            'total_likes': PostRate.objects.filter(liked=True, rated_post=post).count(),
            'total_dislikes': PostRate.objects.filter(liked=False, rated_post=post).count()
        }
        return JsonResponse(data)


"""
class WriteComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(post=Post.objects.filter(pk=self.request.data.get('post')).first())
        serializer.save(posted_by=self.request.user)

class RetrieveComments(generics.ListAPIView):
    serializer_class = PostListSerializer
    lookup_field='pk'
    
    def get_queryset(self):
        post = Post.objects.get(pk=self.kwargs.get(self.lookup_field))
        comments = Comment.objects.filter(post=post)
        return comments

class CommentCount(APIView):

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        data = {
            'comment_count': post.comment_set.all().count(),
        }
        return JsonResponse(data)

def commentedit(request):
    return redirect('/')

def commentdelete(request):
    return redirect('/')
"""