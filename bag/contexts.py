

def bag_contents(request):

    grand_total = 0
    bag_items = 0
    product_count = 0

    context = {
        "bag_items": bag_items,
        "grand_total": grand_total,
        "product_count": product_count,
    }

    return context
