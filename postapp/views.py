from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate

from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView

class IndexView(TemplateView):
    template_name = 'postapp/index.html'

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
