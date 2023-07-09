from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Post, Tag, Category


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserAuthForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'category', 'tags', 'image')
