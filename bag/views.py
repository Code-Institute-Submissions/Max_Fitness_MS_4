from django.shortcuts import render, redirect
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
        if item_id in list(subscription_bag.keys()):
            messages.warning(request, """Item has already been
            added to your bag.""")
        else:
            subscription_bag[item_id] = category
            request.session['subscription_bag'] = subscription_bag
    else:
        if item_id in list(bag.keys()):
            messages.warning(request, """Item has already been
            added to your bag.""")
        else:
            bag[item_id] = category
            request.session['bag'] = bag

    return redirect(redirect_url)
