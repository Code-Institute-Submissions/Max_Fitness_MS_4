from django.shortcuts import render
from blog.models import BlogPost
# Create your views here.


def home_page(request):
    blogPost = BlogPost.objects.order_by('-date_added')[:3]

    context = {
        'blogPost': blogPost,
    }
    return render(request, 'home/index.html', context)
