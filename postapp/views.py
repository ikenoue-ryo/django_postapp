from django.shortcuts import render

from .forms import LoginForm

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

class IndexView(TemplateView):
    template_name = 'postapp/index.html'

class Login(LoginView):
    form_class = LoginForm
    template_name = 'postapp/login.html'

class Logout(LogoutView):
    template_name = 'postapp/index.html'
