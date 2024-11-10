from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL for the list of posts
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # URL for viewing a single post
    path('post/new/', views.post_create, name='post_create'),  # URL for creating a new post
    path('new/', views.post_create, name='post_create'),
]
