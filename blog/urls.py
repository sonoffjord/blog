from django.urls import path

from .views import Home, PostsByCategory, PostsByTag, PostDetail, register, user_login, user_logout, add_post


app_name = 'blog'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cat/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post'),
    path('add/', add_post, name='add'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout')
]
