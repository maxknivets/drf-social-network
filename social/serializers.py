from rest_framework import serializers
from social.models import Post

class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, 
        default=serializers.CurrentUserDefault()
    )
        
    class Meta:
        model = Post
        fields = ['id','user','pub_date','post_text']

