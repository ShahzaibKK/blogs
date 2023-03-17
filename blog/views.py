from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Blog, BlogPost
from .forms import NewBlog, NewBlogPost

# Create your views here.


def index(req):
    blog = Blog.objects.order_by("created_date")
    context = {"blog": blog}
    return render(req, "blog/index.html", context)


def blog_posts(req, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog_posts = blog.blogpost_set.order_by("-created_date")
    context = {"blog": blog, "blog_posts": blog_posts}
    return render(req, "blog/blog_posts.html", context)


def add_blog(req: HttpRequest):
    if req.method != "POST":
        form = NewBlog()
    else:
        form = NewBlog(data=req.POST)
        form.is_valid
        form.save()
        return redirect("blog:index")

    context = {"form": form}
    return render(req, "blog/add_blog.html", context)


def add_post(req, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if req.method != "POST":
        form = NewBlogPost()
    else:
        form = NewBlogPost(data=req.POST)
        form.is_valid()
        new_post = form.save(commit=False)
        new_post.blog = blog
        new_post.save()
        return redirect("blog:blog_posts", blog_id=blog_id)

    context = {"blog": blog, "form": form}
    return render(req, "blog/add_post.html", context)


def edit_post(req, post_id):
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog
    if req.method != "POST":
        form = NewBlogPost(instance=post)
    else:
        form = NewBlogPost(instance=post, data=req.POST)
        form.is_valid()
        form.save()
        return redirect("blog:blog_posts", blog_id=blog.id)

    context = {"blog": blog, "form": form, "post": post}
    return render(req, "blog/edit_post.html", context)
