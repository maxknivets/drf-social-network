from rest_framework import serializers
from social.models import Post, Vote

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
    
        
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
        

