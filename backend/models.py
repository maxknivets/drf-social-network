from django.db import models
from django.contrib.auth.models import User
# class User attributes (https://docs.djangoproject.com/en/2.0/ref/contrib/auth/)
# username,  first_name, last_name, email, password, groups, user_permissions, is_staff, is_active, is_superuser, last_login, date_joined

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100,blank=True)
    profile_picture = models.ImageField(upload_to="profile-pictures", blank=True)
    
    def __str__(self):
        return str(self.user)

class Post(models.Model):
    text = models.CharField(max_length=200)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Publication Date', auto_now=True)
    image = models.ImageField(upload_to='post-images', blank=True)
    in_reply_to_post = models.IntegerField(blank=True, null=True)
    
    def info(self):
        return 'Post Text: %s \nPosted By: %s\nPublished At: %s' % (self.text, self.posted_by, self.pub_date)
    
    def get_readable_date(self):
        return self.pub_date.strftime("%B %d, %Y")
    
    def get_user(self):
        user_dict = vars(self.posted_by)
        return {"id": user_dict["id"], "username": user_dict["username"]}

    def __str__(self):
        return self.text

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    is_followed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='is_followed_by')

    def follows(self, user):
        return Followers.objects.filter(is_followed_by=user)
        
    def followers(self, user):
        followers_list = Followers.objects.filter(user=user).exclude(is_followed_by=user)
        
    def __str__(self):
        return str(self.user)

class PostRate(models.Model):
    liked = models.BooleanField(null=True)
    rated_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.rated_post)
