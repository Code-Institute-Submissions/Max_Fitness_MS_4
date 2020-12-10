from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Product, Category
from django.db.models.functions import Lower
from django.db.models import Q
from django.contrib import messages
# Create your views here.


def products_page(request):
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    current_sorting = None
    if request.GET:
        if 'sort' in request.GET:
            sortKey = request.GET['sort']
            sort = sortKey
            if sortKey == 'Name':
                sortKey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortKey == 'category':
                sortKey = 'category_name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortKey = f'-{sortKey}'
            products = products.order_by(sortKey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               'You did not enter any search criteria!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) |\
                Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)
