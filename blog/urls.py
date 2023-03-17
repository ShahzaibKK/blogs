from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("blog_posts/<int:blog_id>", views.blog_posts, name="blog_posts"),
    path("add_post/<int:blog_id>", views.add_post, name="add_post"),
    path("add_blog", views.add_blog, name="add_blog"),
    path("edit_post/<int:post_id>", views.edit_post, name="edit_post"),
]
