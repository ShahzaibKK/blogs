from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("blog_posts/<int:blog_id>", views.blog_posts, name="blog_posts"),
]
