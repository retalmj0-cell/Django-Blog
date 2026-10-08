from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('users/', views.users_view, name='users'),
    path('blogs/', views.blogs_view, name='blogs'),
    path('comments/', views.comments_view, name='comments'),
    path('categories/', views.categories_view, name='categories'),
    path('blog/<int:post_id>/', views.blogdetails_view, name='blogdetails'),
]