from rest_framework import serializers
from social.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pub_date','post_text', 'image']

class PostEdit(serializers.Serializer):
    post_text = serializers.CharField()

class CommentSerializer(serializers.ModelSerializer):
    in_reply_to_comment = serializers.IntegerField(required=False)
    in_reply_to_user = serializers.IntegerField(required=False)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    class Meta:
        model = Comment
        fields = ['post_date', 'comment', 'in_reply_to_comment', 'in_reply_to_user']


