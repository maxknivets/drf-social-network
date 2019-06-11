from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from social.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pub_date','post_text', 'image']

class PostListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='get_username')
    pub_date = serializers.CharField(source='get_readable_date')

    class Meta:
        model = Post
        fields = ['id','user','pub_date','post_text','image']

class PostEditSerializer(serializers.Serializer):
    post_text = serializers.CharField()

class CommentSerializer(serializers.ModelSerializer):
    in_reply_to_comment = serializers.IntegerField(required=False)
    in_reply_to_user = serializers.IntegerField(required=False)

    class Meta:
        model = Comment
        fields = ['post_date', 'comment', 'in_reply_to_comment', 'in_reply_to_user']


class CommentListSerializer(serializers.ModelSerializer):
    posted_by = serializers.CharField(source='get_username')
    post_date = serializers.CharField(source='get_readable_date')
    in_reply_to_user = serializers.CharField(source='get_user')

    class Meta:
        model = Comment
        fields = ['id','post_date','posted_by','comment', 'in_reply_to_comment', 'in_reply_to_user']


