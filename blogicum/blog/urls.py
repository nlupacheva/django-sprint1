"""URL configuration for blog app."""

from django.urls import path

from . import views

# pylint: disable=C0103
app_name = 'blog'  # namespace приложения

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts'),
]
