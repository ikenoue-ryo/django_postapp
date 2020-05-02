from django import template
from django.utils.safestring import mark_safe
from ..models import Like
register = template.Library()


@register.filter(name='get_likes')
def get_likes(like_list, key):
    text = ""
    if key in like_list:
        text = ""
        for like in like_list[key]:
            text += f"{like.author.profname}, "
        if len(text) >= 1:
            text += "がいいねしました"
    return text


@register.filter(name='is_like')
def is_like(post, user):
    if Like.objects.filter(author=user, post=post).exists():
        return mark_safe(f"<button style=\"border: 0;padding: 0;\" class=\"like\" id=\"{post.id}\" type=\"submit\"><i class=\" fas fa-heart\"></i></button>")
    else:
        return mark_safe(f"<button style=\"border: 0;padding: 0;\" class=\"like\" id=\"{post.id}\" type=\"submit\"><i class=\" far fa-heart\"></i></button>")


@register.filter(name='get_comment_list')
def get_comment_list(comment_list, key):
    text = ""
    if key in comment_list:
        for comment in comment_list[key]:
            text += mark_safe(f"<p><a href=\"profile/{comment.author.profname}\"><img src=\"media/{comment.author.icon}\"></a></p>")
            text += mark_safe(f"<p class=\"comment\">{comment.text}</p>")
            text += mark_safe(f"<p class=\"comment-delete\"><a href=\"delete/comment/{comment.id}/\" value=\"DELETE\" data-toggle=\"modal\" data-target=\"#commentDelete-{comment.id}\"><i class=\"far fa-trash-alt\"></i></a></p>")
    return mark_safe(text)


# タグ一覧表示用ここから
@register.filter(name='get_comment_list2')
def get_comment_list2(comment_list, key):
    text = ""
    if key in comment_list:
        for comment in comment_list[key]:
            text += mark_safe(f"<p><img src=\"{comment.author.icon.url}\"></p>")
            text += mark_safe(f"<p class=\"comment\">{comment.text}</p>")
            text += mark_safe(f"<p class=\"comment-delete\"><a href=\"delete/comment/{comment.id}/\" value=\"DELETE\" data-toggle=\"modal\" data-target=\"#commentDelete-{comment.id}\"><i class=\"far fa-trash-alt\"></i></a></p>")
    return mark_safe(text)
# タグ一覧表示用ここまで
