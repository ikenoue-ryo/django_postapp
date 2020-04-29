from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.views.decorators.http import require_POST
from django.views import View
from django.views import generic
from django.db.models import Count, Q
from .forms import LoginForm, SignUpForm, PostForm, ProfileForm
from .models import Post, Like, Comment, Tag
from users.models import User


class IndexView(ListView):
    model = Post
    template_name = 'postapp/index.html'
    paginate_by = 12
    queryset = Post.objects.order_by('created_at').reverse().annotate(Count('like', distinct=True), Count('comment', distinct=True))

    """ 検索機能 Text or Tag """
    def get_queryset(self):
        q_word = self.request.GET.get('keyword')

        if q_word:
            object_list = Post.objects.order_by('created_at').reverse().annotate(Count('like', distinct=True), Count('comment', distinct=True)).filter(Q(text__icontains=q_word) | Q(tag__name__icontains=q_word))
            messages.info(self.request, '{} の検索結果'.format(q_word))
        else:
            object_list = Post.objects.order_by('created_at').reverse().annotate(Count('like', distinct=True), Count('comment', distinct=True))
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        like_list = {}
        comment_list = {}
        for post in context['post_list']:
            like_list[post.id] = Like.objects.filter(post=post)
            comment_list[post.id] = Comment.objects.filter(post=post)
        context['like_list'] = like_list
        context['comment_list'] = comment_list
        return context


""" タグ一覧 """
class Tag(DetailView):
    model = Tag
    template_name = 'postapp/tag_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["posts_list"] = Post.objects.all().annotate(Count('like', distinct=True), Count('comment', distinct=True))
        # context["posts_list"] = Post.objects.get(id=self.kwargs['pk']).annotate(Count('like', distinct=True), Count('comment', distinct=True))
        like_list = {}
        comment_list = {}
        for post in context['posts_list']:
            like_list[post.id] = Like.objects.filter(post=post)
            comment_list[post.id] = Comment.objects.filter(post=post)
        context['like_list'] = like_list
        context['comment_list'] = comment_list
        return context


class New(CreateView):
    template_name = 'postapp/new.html'
    form_class = PostForm
    success_url = reverse_lazy('postapp:index')

    #ログインユーザーを投稿者として登録する
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(New, self).form_valid(form)


class Edit(UpdateView):
    template_name = 'postapp/edit.html'
    model = Post
    fields = ('picture1', 'picture2', 'picture3', 'picture4', 'text')
    success_url = reverse_lazy('postapp:index')


class Delete(DeleteView):
    model = Post
    success_url = reverse_lazy('postapp:index')


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'postapp/signup.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('profname')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('postapp:index')
        return render(request, 'postapp/signup.html', {'form': form})


class Login(LoginView):
    form_class = LoginForm
    template_name = 'postapp/login.html'
    

class Logout(LogoutView):
    template_name = 'postapp/index.html'


class ProfileView(DetailView):
    model = User
    template_name = 'postapp/profile.html'


class ProfileEditView(UpdateView):
    model = User
    # form_class = ProfileForm
    fields = ['icon', 'proftext']
    # success_url = reverse_lazy('postapp:index')

    def get_object(self):
        # ログイン中のユーザーで検索することを明示する
        return self.request.user

    def get_success_url(self):
           userid = self.kwargs['pk']
           return reverse_lazy('postapp:profile', kwargs={'pk': userid})



class Likes(View):
    model = Like
    slug_field = 'post'# モデルのフィールドの名前
    slug_url_kwarg = 'postId'# urls.pyでのキーワードの名前

    def get(self, request, postId):
        post = Post.objects.get(id=postId)
        like = Like.objects.filter(author=self.request.user, post=post)
        like_list = {}
        comment_list = {}
        # 過去にいいねを押しているのか
        if like.exists():
            # いいねされていれば消す
            like.delete()
        else: 
            # いいねされていなければ追加する
            like = Like(author=self.request.user, post=post)
            like.save()
        like_list[post.id] = Like.objects.filter(post=post)
        comment_list[post.id] = Comment.objects.filter(post=post)
        return render(request, 'postapp/like.html', {
            'like_list': like_list,
            'comment_list': comment_list,
            'post': post
        })


class AddComment(View):
    def post(self, request, postId):
        like_list = {}
        comment_list = {}

        post = Post.objects.get(id=postId)
        text = request.POST["comment"]

        comment = Comment(author=self.request.user, post=post, text=text)
        comment.save()

        like_list[post.id] = Like.objects.filter(post=post)
        comment_list[post.id] = Comment.objects.filter(post=post)
        return render(request, 'postapp/comment.html', {
            'like_list': like_list,
            'comment_list': comment_list,
            'post': post
        })


class DeleteComment(DeleteView):
    model = Comment
    template_name = 'postapp/comment_delete.html'
    success_url = reverse_lazy('postapp:index')
