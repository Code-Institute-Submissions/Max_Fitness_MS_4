from django.shortcuts import render, redirect, reverse
from django.contrib import messages


from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    subscription_bag = request.session.get('subscription_bag', {})

    if not bag and not subscription_bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context)
