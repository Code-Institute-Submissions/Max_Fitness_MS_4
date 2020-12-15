from django.shortcuts import render, redirect, reverse
from django.contrib import messages
import os

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    subscription_bag = request.session.get('subscription_bag', {})

    if not bag and not subscription_bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': os.getenv('STRIPE_PUBLIC_KEY'),
        'client_secret': os.getenv('STRIPE_SECRET_KEY'),
    }

    return render(request, template, context)
