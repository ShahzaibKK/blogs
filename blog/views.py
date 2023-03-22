from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404
from .models import Blog, BlogPost
from .forms import NewBlog, NewBlogPost
from django.contrib.auth.decorators import login_required


# Create your views here.
def check_authors(blog, req):
    if req.user != blog.author:
        raise Http404


def index(req: HttpRequest):
    if req.user.is_authenticated:
        blog = Blog.objects.filter(author=req.user).order_by("created_date")
    else:
        blog = None
    context = {"blog": blog}
    return render(req, "blog/index.html", context)


@login_required
def blog_posts(req, blog_id):
    blog = Blog.objects.get(id=blog_id)
    check_authors(blog, req)
    blog_posts = blog.blogpost_set.order_by("-created_date")
    context = {"blog": blog, "blog_posts": blog_posts}
    return render(req, "blog/blog_posts.html", context)


@login_required
def add_blog(req: HttpRequest):
    if req.method != "POST":
        form = NewBlog()
    else:
        form = NewBlog(data=req.POST)
        form.is_valid
        new_blog = form.save(commit=False)
        new_blog.author = req.user
        new_blog.save()
        return redirect("blog:index")

    context = {"form": form}
    return render(req, "blog/add_blog.html", context)


@login_required
def add_post(req, blog_id):
    blog = Blog.objects.get(id=blog_id)
    check_authors(blog, req)
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


@login_required
def edit_post(req, post_id):
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog
    check_authors(blog, req)
    if req.method != "POST":
        form = NewBlogPost(instance=post)
    else:
        form = NewBlogPost(instance=post, data=req.POST)
        form.is_valid()
        form.save()
        return redirect("blog:blog_posts", blog_id=blog.id)

    context = {"blog": blog, "form": form, "post": post}
    return render(req, "blog/edit_post.html", context)
