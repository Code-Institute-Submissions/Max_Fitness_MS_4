from django.shortcuts import render
from .models import BlogPost
# Create your views here.


def render_blog(request):
    """
    Renders blog page for the user
    """
    allPosts = BlogPost.objects.all()
    print(allPosts)

    template = "blog/blogs.html"
    context = {
        'blogPosts': allPosts,
    }
    return render(request, template, context)
