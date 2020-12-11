from products.models import Product
from django.shortcuts import get_object_or_404


def bag_contents(request):

    total = 0
    product_count = 0
    bag_items = []
    bag = request.session.get('bag', {})

    for item_id, name in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        product_count += 1
        bag_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
    }

    return context
