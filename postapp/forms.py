from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from .models import Post


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'profname', 'icon')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('picture1', 'picture2', 'picture3', 'picture4', 'text')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('icon', 'proftext')

    def __init__(self, email=None, profname=None, icon=None, proftext=None):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        #ユーザーの更新前の情報を挿入
        if email:
            self.fields['email'].widget.attrs['values'] = email
        if profname:
            self.fields['profname'].widget.attrs['values'] = profname
        if icon:
            self.fields['icon'].widget.attrs['values'] = icon
        if proftext:
            self.fields['proftext'].widget.attrs['values'] = proftext

    def update(self, user):
        user.icon = self.cleaned_data['icon']
        user.proftext = self.cleaned_data['proftext']
        user.save()
