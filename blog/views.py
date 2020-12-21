from django.shortcuts import render

# Create your views here.


def render_blog(request):
    """
    Renders blog page for the user
    """
    template = "blog/blogs.html"
    context = {

    }
    return render(request, template, context)
