from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.db.models import F
from django.contrib.auth import login, logout

from .models import Post, Category, Tag
from .forms import UserRegisterForm, UserAuthForm, AddPostForm


class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context


class PostsByCategory(ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 6
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostsByTag(ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 6
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:home')
    else:
        form = AddPostForm()
    return render(request, template_name='blog/formtemplate.html', context={'form': form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')
    else:
        form = UserRegisterForm()
    return render(request, template_name='blog/formtemplate.html', context={'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserAuthForm(data=request.POST)
        if form.is_valid():
            user  = form.get_user()
            login(request, user)
            return redirect('blog:home')
    else:
        form = UserAuthForm()
    return render(request, template_name='blog/formtemplate.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('blog:login')