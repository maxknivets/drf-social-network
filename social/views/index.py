from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from social.models import Post#, Followers
from social.forms import PostForm, EditForm, DeleteForm, CommentForm


def index(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[::1]
    last_post = Post.objects.get_queryset().last()
    return render(request, 'social/index.html', {'latest_posts_list':posts, 'latest_post':last_post, 'postform':PostForm(), 'editform':EditForm(), 'commentform':CommentForm()})


#class Index(LoginRequiredMixin, generic.ListView):
#    model = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[::1]
#    context_object_name = 'latest_posts_list'
    
#    def get_context_data(self, **kwargs):
#        context = super(Index, self).get_context_data(**kwargs)
#        context['latest_post'] = Post.objects.get_queryset().last()
#        return context




#        following_list = []
#        for follows in Followers.objects.filter(is_followed_by=request.user):
#            following_list.append(follows.user.username)

