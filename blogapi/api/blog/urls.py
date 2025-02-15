from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, UserViewSet

router = DefaultRouter()
router.register(r'blogposts', BlogPostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]