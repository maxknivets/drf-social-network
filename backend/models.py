from django.db import models
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_authenticated_user

# A primitive extension of the standard User table from Django lib
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile-pictures", null=True, blank=True)

    def get_user_id(self):
        return self.user.pk

    def get_username(self):
        return self.user.username

    def get_followers_count(self):
        return Follower.objects.filter(user = self.user).exclude(is_followed_by = self.user).count()

    def get_following_count(self):
        return Follower.objects.filter(is_followed_by = self.user).count()

    def get_follow_status(self):
        follow_status = Follower.objects.filter(user = self.user, is_followed_by = get_current_authenticated_user())
        return "Following" if follow_status else "Follow"

    def get_profile_belongs_to_authenticated_user(self):
        return self.user == get_current_authenticated_user()
        
    def __str__(self):
        return str(self.user)

class Post(models.Model):
    text = models.CharField(max_length=200)
    posted_by = CurrentUserField(related_name='posted_by')
    pub_date = models.DateTimeField('Publication Date', auto_now=True)
    image = models.ImageField(upload_to='post-images', null=True)
    in_reply_to_post = models.IntegerField(null=True)

    def get_readable_date(self):
        return self.pub_date.strftime("%B %d, %Y")

    def get_post_belongs_to_authenticated_user(self):
        return self.posted_by.pk == get_current_authenticated_user().pk

    def get_user(self):
        user_dict = vars(self.posted_by)
        return {"id": user_dict["id"], "username": user_dict["username"]}

    def get_likes_count(self):
        return PostRate.objects.filter(liked=True, rated_post=self).count()

    def get_dislikes_count(self):
        return PostRate.objects.filter(liked=False, rated_post=self).count()

    def get_comments(self):
        return Post.objects.filter(in_reply_to_post=self.pk)

    def get_comments_count(self):
        return Post.objects.filter(in_reply_to_post=self.pk).count()

    def __str__(self):
        return str(self)

class PostRate(models.Model):
    liked = models.BooleanField(null=True)
    rated_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.rated_post)

class Follower(models.Model): #rename model to UserFollows or find a better name
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    is_followed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='is_followed_by')

    def get_user_info(self):
        user_dict = vars(self.user)
        return {"id": user_dict["id"], "username": user_dict["username"]}

    def get_is_followed_by_info(self):
        user_dict = vars(self.is_followed_by)
        return {"id": user_dict["id"], "username": user_dict["username"]}
        
    def get_following(self, user):
        return Follower.objects.filter(is_followed_by=user)

    def get_followers(self, user):
        return Follower.objects.filter(user=user).exclude(is_followed_by=user)

    def get_following_count(self, user):
        return Follower.objects.filter(is_followed_by=user).count()

    def get_followers_count(self, user):
        return Follower.objects.filter(user=user).count()
        
    def __str__(self):
        return str(self)