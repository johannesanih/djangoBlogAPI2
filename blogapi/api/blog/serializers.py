from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    likes = serializers.ReadOnlyField()
    class Meta:
        model = BlogPost
        fields = ["id", "url", "owner", "title", "body", "likes", "created"]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    blogposts = serializers.HyperlinkedRelatedField(many=True, view_name="blogpost-detail", read_only=True)
    class Meta:
        model = User
        fields = ["id", "url", "username", "blogposts"]