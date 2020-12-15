from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


# Create your views here.

def checkout(request):
    # Get stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Get bag items
    bag = bag_contents(request)
    bag_items = bag['bag_items']

    # Redirect if there are no items in the bag
    if not bag_items:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    # Sum price of current items in the shopping bag
    total = bag['total']
    stripe_total = round(total * 100)

    # Set up Stripe and create Payment Intent
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_secret_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your enviroment?')

    # Create form
    order_form = OrderForm()

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
