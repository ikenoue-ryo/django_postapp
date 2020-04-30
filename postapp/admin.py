from django.contrib import admin
from .models import Post, Like, Tag, Comment, Connection

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Connection)
