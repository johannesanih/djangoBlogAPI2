from django.db import models

# Create your models here.
class BlogPost(models.Model):
    owner = models.ForeignKey('auth.User', related_name='blogposts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField()
    likes = models.BigIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
