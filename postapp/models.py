from django.db import models
from users.models import User


class Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to='image/posts/', blank=False, null=False)
    picture2 = models.ImageField(upload_to='image/posts/', blank=True, null=True)
    picture3 = models.ImageField(upload_to='image/posts/', blank=True, null=True)
    picture4 = models.ImageField(upload_to='image/posts/', blank=True, null=True)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class Like(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('postapp.Post', on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('postapp.Post', on_delete=models.CASCADE)
    text = models.TextField(blank=True)
