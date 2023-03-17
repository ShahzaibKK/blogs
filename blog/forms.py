from django import forms
from .models import Blog, BlogPost


class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "description"]
        lebels = {"title": "", "description": ""}
        widgets = {"description": forms.Textarea(attrs={"cols": 80})}


class NewBlogPost(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content"]
        lebels = {
            "title": "",
            "content": "",
        }
