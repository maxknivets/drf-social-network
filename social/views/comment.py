from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.utils.html import escape
from social.models import User, Vote, Comment, Post
from social.forms import EditForm, DeleteForm, CommentForm
from rest_framework import generics
from rest_framework.response import Response

def comment(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('id')
            post = get_object_or_404(Post, pk=post_id)
            
            comment = form.cleaned_data.get('comment')
            in_reply_to_user = form.cleaned_data.get('in_reply_to_user')
            in_reply_to_comment = form.cleaned_data.get('in_reply_to_comment')
            date = timezone.now()
            data = {}
            new_comment = Comment(comment=comment, post_date=date, posted_by=request.user, post=post)
            
            if in_reply_to_user and in_reply_to_comment:
                new_comment.in_reply_to_user=in_reply_to_user
                new_comment.in_reply_to_comment=in_reply_to_comment
                data['in_reply_to_user']=in_reply_to_user
                data['in_reply_to_comment']=in_reply_to_comment
                data['get_username']=new_comment.get_user().username
            else:
                data['in_reply_to_user']=None
                data['in_reply_to_comment']=None
            
            new_comment.save()
            
            data['post_id']=post_id
            data['comment_text']=escape(new_comment.comment)
            data['comment_pk']=new_comment.pk
            data['posted_by']=new_comment.posted_by.username
            data['user_id']=new_comment.posted_by.pk
            data['date']=new_comment.get_readable_date()
            
            return JsonResponse(data)
    return redirect('/')

#class CommentOnPost(generics.CreateAPIView):

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


