from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BlogPostSerializer, UserSerializer
from .models import BlogPost
from django.contrib.auth.models import User

# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer