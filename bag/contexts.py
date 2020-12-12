from products.models import Product
from subscriptions.models import Membership
from django.shortcuts import get_object_or_404


def bag_contents(request):

    total = 0
    product_count = 0
    bag_items = []
    bag = request.session.get('bag', {})
    subscription_bag = request.session.get('subscription_bag', {})

    for item_id, category in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        product_count += 1
        bag_items.append({
            'item_id': item_id,
            'category': category,
            'product': product,
        })

    for item_id, category in subscription_bag.items():
        subscription = get_object_or_404(Membership, pk=item_id)
        total += subscription.price
        product_count += 1
        bag_items.append({
            'item_id': item_id,
            'category': category,
            'subscription': subscription,
        })

    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
    }

    return context
