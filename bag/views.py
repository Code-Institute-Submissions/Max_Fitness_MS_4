from django.shortcuts import render, redirect, HttpResponse
from products.models import Product
from subscriptions.models import Membership
from django.contrib import messages

# Create your views here.


def view_bag(request):
    """ Return Bag Page """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Add item to bag """

    category = request.POST.get('category')
    subscriptionType = None
    if 'subscriptionType' in request.POST:
        subscriptionType = request.POST.get('subscriptionType')
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})
    subscription_bag = request.session.get('subscription_bag', {})

    if subscriptionType:
        membership = Membership.objects.get(pk=item_id)
        if item_id in list(subscription_bag.keys()):
            messages.info(request, f"""{membership.name} has already been
            added to your bag.""")
        else:
            subscription_bag[item_id] = category
            request.session['subscription_bag'] = subscription_bag
            messages.success(request, f"""{membership.name} has been
            added to your bag.""")
    else:
        product = Product.objects.get(pk=item_id)
        if item_id in list(bag.keys()):
            messages.info(request, f"""{product.name} has already been
            added to your bag.""")
        else:
            bag[item_id] = category
            request.session['bag'] = bag
            messages.success(request, f"""{product.name} has been
            added to your bag.""")

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    try:
        subscriptionType = None
        if 'subscriptionType' in request.POST:
            subscriptionType = request.POST.get('subscriptionType')
        bag = request.session.get('bag', {})
        subscription_bag = request.session.get('subscription_bag', {})

        if subscriptionType:
            membership = Membership.objects.get(pk=item_id)
            subscription_bag.pop(item_id)
            request.session['subscription_bag'] = subscription_bag
            messages.info(request, f"""{membership.name} has been
            removed from your bag.""")

        else:
            product = Product.objects.get(pk=item_id)
            request.session['bag'] = bag
            bag.pop(item_id)
            messages.info(request, f"""{product.name} has been
            removed from your bag.""")

        return HttpResponse(status=200)

    except Exception as e:
        print(e)
        return HttpResponse(status=500)
