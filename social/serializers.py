from rest_framework import serializers
from social.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pub_date','post_text', 'image']

    
