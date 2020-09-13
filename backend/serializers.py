from rest_framework import serializers
from backend.models import Post, PostRate, Profile, Follower
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'get_username')
    user_id = serializers.IntegerField(source = 'get_user_id')
    followers_count = serializers.IntegerField(source = 'get_followers_count')
    following_count = serializers.IntegerField(source = 'get_following_count')
    profile_belongs_to_authenticated_user = serializers.BooleanField(source = 'get_profile_belongs_to_authenticated_user')
    follow_status = serializers.CharField(source = 'get_follow_status')
    
    class Meta:
        model = Profile
        fields = ('username', 'user_id', 'followers_count', 'following_count', 'profile_belongs_to_authenticated_user', 'follow_status', 'first_name', 'last_name', 'bio', 'location')
        read_only_fields = ('username', 'user_id', 'followers_count', 'following_count', 'profile_belongs_to_authenticated_user', 'follow_status')

class FollowerSerializer(serializers.ModelSerializer):
    user = serializers.DictField(child = serializers.CharField(), source = 'get_user_info', read_only = True)
    is_followed_by = serializers.DictField(child = serializers.CharField(), source = 'get_is_followed_by_info', read_only = True)

    class Meta:
        model = Follower
        fields = ('user', 'is_followed_by')
        read_only_fields = ('user', 'is_followed_by')

# Serializer for when someone signs up, currently unused
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], None, validated_data['password'])
        return user

class PostSerializer(serializers.ModelSerializer):
    post_belongs_to_authenticated_user = serializers.BooleanField(source = 'get_post_belongs_to_authenticated_user', read_only = True)
    posted_by = serializers.DictField(child = serializers.CharField(), source = 'get_user', read_only = True)
    pub_date = serializers.CharField(source = 'get_readable_date', read_only = True)

    likes_count = serializers.IntegerField(source='get_likes_count', read_only = True)
    dislikes_count = serializers.IntegerField(source='get_dislikes_count', read_only = True)
    comments_count = serializers.IntegerField(source='get_comments_count', read_only = True)

    class Meta:
        model = Post
        fields = ['id', 'post_belongs_to_authenticated_user', 'posted_by', 'pub_date', 'text', 'image', 'in_reply_to_post', 'likes_count', 'dislikes_count', 'comments_count']
        write_only_fields = ['text', 'image', 'in_reply_to_post']
        
class PostRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostRate
        fields = ['liked', 'rated_post']