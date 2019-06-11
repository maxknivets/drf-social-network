from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.utils.html import escape
from social.models import User, Vote, Comment, Post
from social.forms import EditForm, DeleteForm, CommentForm
from social.serializers import CommentSerializer, CommentListSerializer	
from rest_framework import generics
from rest_framework.response import Response

class WriteComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(post=Post.objects.filter(pk=self.request.data.get('post')).first())
        serializer.save(posted_by=self.request.user)

class RetrieveComments(generics.ListAPIView):
    serializers_class = CommentListSerializer
    lookup_field='pk'
    
    def get_queryset(self):
        import pdb; pdb.set_trace()
        post = Post.objects.filter(pk=self.kwargs.get(self.lookup_field))
        comments = Comment.objects.filter(post=post)
        return comments

def commentedit(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            comment_id = form.cleaned_data.get('id')
            comment = get_object_or_404(Comment, pk=comment_id)
            if request.user == comment.posted_by:
                new_text = form.cleaned_data.get('new_text')
                comment.comment = new_text
                comment.save()
                data = { 'new_text': escape(new_text) }
                return JsonResponse(data)
    return redirect('/')



def commentdelete(request):
    if request.user.is_authenticated:
        comment_id = request.GET.get('id')
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user == comment.posted_by:
            comment.delete()
            data = { 'comment_id': comment_id }
            return JsonResponse(data)
    return redirect('/')


