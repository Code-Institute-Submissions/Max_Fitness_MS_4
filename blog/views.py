from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
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
    query = None

    if request.GET:

        # Sorting logic for blog posts
        # sorts blog posts by date
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

        # Query logic for blog posts objects
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               'You did not enter any search criteria!')
                return redirect(reverse('blog'))
            queries = Q(title__icontains=query) |\
                Q(body__icontains=query)
            allPosts = allPosts.filter(queries)

    current_sorting = f'{sort}_{direction}'
    template = "blog/blogs.html"
    context = {
        'search_term': query,
        'blogPosts': allPosts,
        'current_sorting': current_sorting,
    }
    return render(request, template, context)
