from django.urls import path

from .views import index, get_category


app_name = 'blog'

urlpatterns = [
    path('', index, name='home'),
    path('cat/<str:slug>/', get_category, name='category'),
]
