from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name='blog-home'),
    path("users/<str:username>", UserPostListView.as_view(), name='user-posts'),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name='blog-about'),
]