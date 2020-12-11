from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def view_bag(request):
    """ Return Bag Page """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Add item to bag """

    itemName = request.POST.get('name')
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        messages.warning(request, f"""Item {itemName} has already
         been added to your bag.""")
    else:
        bag[item_id] = itemName

    request.session['bag'] = bag

    return redirect(redirect_url)
