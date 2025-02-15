from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    likes = serializers.ReadOnlyField()
    class Meta:
        fields = ["owner", "title", "body", "likes", "created"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "username"]