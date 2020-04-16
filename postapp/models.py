from django.db import models
from users.models import User


class Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to='image/posts/', blank=False, null=False)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
