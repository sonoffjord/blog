from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title',]

    def  __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:category", kwargs={"slug": self.slug})
    

class Tag(models.Model):
    title = models.CharField(max_length=80, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Теги'
        ordering = ['title',]

    def  __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    content = models.TextField(verbose_name='Текст поста')
    created_at = models.DateField(
        auto_now_add=True, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='image/%Y/%m/%d', blank=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Тэг')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at',]

    def  __str__(self):
        return self.title
