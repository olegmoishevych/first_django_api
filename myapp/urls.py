from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('api/posts/', views.blog_posts, name='blog_posts'),
  path('api/posts/<int:post_id>/', views.delete_blog_post, name='delete_blog_post'),
  path('api/posts/update/<int:post_id>/', views.update_blog_post, name='update_blog_post'),
]


