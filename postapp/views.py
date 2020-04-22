from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.views import generic
from .forms import LoginForm, SignUpForm, PostForm, ProfileForm
from .models import Post, Like, Comment, #Tag
from users.models import User


class IndexView(ListView):
    model = Post
    template_name = 'postapp/index.html'
    paginate_by = 12
    queryset = Post.objects.order_by('created_at').reverse()

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

 
# """ タグ一覧 """
# class Tag(generic.ListView):
#     model = Post
#     template_name = 'postapp/index.html'

#     def get_queryset(self):
#         tag = Tag.objects.get(name=self.kwargs['tag'])
#         queryset = Post.objects.order_by('-id').filter(tag=tag)
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tag_key'] = self.kwargs['tag']
#         return context


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
    form_class = PostForm
    success_url = reverse_lazy('postapp:index')


# class Update(UpdateView):
#     model = Post
#     fields = ('picture1', 'picture2', 'picture3', 'picture4', 'text', 'tag')
#     success_url = reverse_lazy('postapp:index')


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

    users = User.objects.all()
    for user in users:
        posts = user.post_set.all()


class ProfileEditView(UpdateView):
    model = get_user_model()
    form_class = ProfileForm
    fields = ['icon', 'proftext']
    success_url = reverse_lazy('postapp:profile')

    def get_object(self):
        # ログイン中のユーザーで検索することを明示する
        return self.request.user


class Likes(View):
    model = Like
    slug_field = 'post'
    slug_url_kwarg = 'postId'

    def get(self, request, postId):
        post = Post.objects.get(id=postId)
        like = Like.objects.filter(author=self.request.user, post=post)
        like_count = Like.objects.filter(id=postId).count()
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
            #'like_count': like_count
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
        return render(request, 'postapp/like.html', {
            'like_list': like_list,
            'comment_list': comment_list,
            'post': post
        })


