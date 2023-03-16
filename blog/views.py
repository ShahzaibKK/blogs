from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, BlogPost

# Create your views here.


def index(req):
    blog = Blog.objects.order_by("created_date")
    context = {"blog": blog}
    return render(req, "blog/index.html", context)


def blog_posts(req, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog_posts = blog.blogpost_set.all()
