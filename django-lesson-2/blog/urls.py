from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_archive, name='blog_archive'),
    path('<int:article_id>/', views.blog_post, name='blog_post'),
]
