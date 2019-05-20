from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.utils.html import escape
from social.models import User, Post, Vote
from social.forms import PostForm, EditForm, DeleteForm
from social.serializers import PostSerializer, VoteSerializer
from rest_framework import generics

def post(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('post_text')
            image = request.FILES.get('post_image')
            date = timezone.now()            
            post = Post(post_text=text, user=request.user, pub_date=date)
            if image:
                post = Post(post_text=text, user=request.user, pub_date=date, image=image)
            post.save()

            data = {}
            data['post_image'] = None
            if image:
                data['post_image'] = post.image.url
            data['post_text'] = escape(post.post_text)
            data['post_date'] = post.get_readable_date()
            data['post_id'] = post.pk
            data['user_id'] = request.user.pk
            data['username'] = request.user.username
            return JsonResponse(data)    
    return redirect('/')



def databasecheck(request, post_id):
    if request.user.is_authenticated:
        data={'currentId':Post.objects.last().pk, 'lastId':post_id}
        return JsonResponse(data)
    return redirect('/')

            
class GetPostInfo(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class VoteOnPost(generics.CreateAPIView):
    serializer_class = VoteSerializer

    def get_queryset(self):
        queryset = Vote.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        user = self.request.user
               

def edit(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('id')
            post = get_object_or_404(Post, pk=post_id)
            if request.user == post.user:
                new_text = form.cleaned_data.get('new_text')
                post.post_text = new_text
                post.save()
                data = { 'new_text': escape(new_text) }
                return JsonResponse(data)
    return redirect('/')



def delete(request):
    if request.user.is_authenticated:
        post_id = request.GET.get('id')
        post = get_object_or_404(Post, pk=post_id)
        if request.user == post.user:
            post.delete()
            data = { 'post_id': post_id }
            return JsonResponse(data)
    return redirect('/')


