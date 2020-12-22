from django.shortcuts import render
from .models import BlogPost
# Create your views here.


def render_blog(request):
    """
    Renders blog page for the user
    """
    allPosts = BlogPost.objects.all()
    sort = None
    direction = None
    current_sorting = None

    if request.GET:
        if 'sort' in request.GET:
            sortKey = request.GET['sort']
            sort = sortKey
            if sortKey == 'date':
                sortKey = 'date_added'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortKey = f'-{sortKey}'
            allPosts = allPosts.order_by(sortKey)

    current_sorting = f'{sort}_{direction}'
    template = "blog/blogs.html"
    context = {
        'blogPosts': allPosts,
        'current_sorting': current_sorting,
    }
    return render(request, template, context)
