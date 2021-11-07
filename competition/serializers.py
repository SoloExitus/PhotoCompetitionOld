from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import PhotoPost, UserProfile

class UserProfileSerializer(ModelSerializer):
    username = serializers.CharField(source='user.username', max_length=256, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'avatar')


class PhotoPostSerializer(ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    author = UserProfileSerializer(source='user')

    class Meta:
        model = PhotoPost
        fields = ('id', 'title', 'description', 'published_date', 'image', 'likes_count', 'comments_count', 'author')