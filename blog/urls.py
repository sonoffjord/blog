from django.urls import path

from .views import Home, get_category, get_post


app_name = 'blog'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cat/<str:slug>/', get_category, name='category'),
    path('post/<str:slug>/', get_post, name='post'),
]
