from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from django.views.decorators.http import require_POST
from .models import BlogPost, BlogComments
from .forms import BlogPostForm
# Create your views here.


def render_blog(request):
    """
    Renders blog page and handles POST request
    to create blog post
    """
    form = None
    if request.user.is_superuser:
        form = BlogPostForm()
    allPosts = BlogPost.objects.all()
    sort = None
    direction = None
    current_sorting = None
    query = None

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add product. \
                 Please ensure the form is valid!')

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
        'blog_form': form,
    }
    return render(request, template, context)


def render_specific_post(request, item_id):
    """
    Renders specific blog post
    """
    blogPost = get_object_or_404(BlogPost, pk=item_id)
    form = None
    if request.user.is_superuser:
        form = BlogPostForm(initial={
            'title': blogPost.title,
            'intro': blogPost.intro,
            'body': blogPost.body,
            'date_added': blogPost.date_added,
            'image_url': blogPost.image_url,
            'image': blogPost.image,
        })

    comments = BlogComments.objects.all()

    postcomments = comments.filter(blog_post__in=item_id)

    template = 'blog/blog_post.html'
    context = {
        "post": blogPost,
        "comments": postcomments,
        "blog_form": form,
    }

    return render(request, template, context)


@require_POST
def update_post(request, item_id):
    blogPost = get_object_or_404(BlogPost, pk=item_id)

    form = BlogPostForm(request.POST, request.FILES, instance=blogPost)
    if form.is_valid():
        form.save()
        title = request.POST['title']
        messages.success(request, f'Blog post {title} \
        has been updated successfully')
        return redirect(reverse('blog_post', args=(item_id,)))

    else:
        messages.error(request, f'Failed to update {title} \
            Try again later.')
        return redirect(reverse('blog_post', args=(item_id,)))
