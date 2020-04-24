from django.db import models
from users.models import User


class Tag(models.Model):
    name = models.CharField('タグ', max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to='image/posts/', blank=False, null=False)
    picture2 = models.ImageField(upload_to='image/posts/', blank=True, null=True)
    picture3 = models.ImageField(upload_to='image/posts/', blank=True, null=True)
    picture4 = models.ImageField(upload_to='image/posts/', blank=True, null=True)
    text = models.TextField(blank=True)
    tag = models.ManyToManyField(Tag, verbose_name='タグ')
    #relationは関連する記事がない場合記事を指定せずに保存できる。Postと紐づけるからself
    relation = models.ManyToManyField('self', verbose_name='関連', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.text


class Like(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('postapp.Post', on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('postapp.Post', on_delete=models.CASCADE)
    text = models.TextField(blank=True)
