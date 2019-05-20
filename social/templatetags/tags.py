from django import template
from social.models import Followers, Comment, Vote

register = template.Library()

@register.simple_tag
def total_likes(post):
    return Vote.objects.filter(vote__in=('L')).count()

@register.simple_tag
def total_dislikes(post):
    return Vote.objects.filter(vote__in=('D')).count()

@register.simple_tag
def total_followers(user):
    return Followers.objects.filter(user=user).count()
    
@register.simple_tag
def total_followed(user):
    return Followers.objects.filter(is_followed_by=user).count()

@register.simple_tag
def already_followed(user, followed_by):
    following = Followers.objects.filter(user=user, is_followed_by=followed_by)
    if following:
        return "Unfollow"
    else:
        return "Follow"

@register.simple_tag
def replies(in_reply_to_comment):
    return Comment.objects.filter(in_reply_to_comment=in_reply_to_comment)
