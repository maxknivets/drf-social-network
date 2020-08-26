from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from backend.models import Post, PostRate
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], None, validated_data['password'])
        return user

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['posted_by', 'text', 'image', 'in_reply_to_post']

class PostRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRate
        fields = ['liked', 'rated_post']

class PostListSerializer(serializers.ModelSerializer):
    posted_by = serializers.DictField(child=serializers.CharField(), source='get_user')
    pub_date = serializers.CharField(source='get_readable_date')

    class Meta:
        model = Post
        fields = ['id', 'posted_by', 'pub_date', 'text', 'image']