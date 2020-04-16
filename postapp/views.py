from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import LoginForm, SignUpForm, PostForm
from .models import Post

from django.views.generic import TemplateView, ListView, CreateView

class IndexView(ListView):
    model = Post
    template_name = 'postapp/index.html'
    paginate_by = 12
    queryset = Post.objects.order_by('created_at').reverse()


class New(CreateView):
    template_name = 'postapp/new.html'
    form_class = PostForm
    success_url = reverse_lazy('postapp:index')

    #ログインユーザーを投稿者として登録する
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(New, self).form_valid(form)


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'postapp/signup.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
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
