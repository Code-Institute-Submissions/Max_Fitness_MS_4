from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

# Models
from .models import OrderLineItem, Order
from products.models import Product
from subscriptions.models import Membership

# Form
from .forms import OrderForm

# Context function
from bag.contexts import bag_contents

import stripe


# Create your views here.

def checkout(request):
    """
    Handle checkout page and checkout form POST request
    """
    # Get bag items
    bag = bag_contents(request)
    bag_items = bag['bag_items']

    # Redirect if there are no items in the bag
    if not bag_items:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    # Get stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if not stripe_secret_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your enviroment?')

    # Sum price of current items in the shopping bag
    total = bag['total']
    stripe_total = round(total * 100)

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        # If the form is valid it will loop through bag items
        # and use them to create instance of OrderLineItem for each.
        if order_form.is_valid():
            order = order_form.save()
            for item in bag_items:
                print(item)
                if item['category'] != "membership":
                    try:
                        product = get_object_or_404(Product, pk=item['item_id'])
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            price=product.price,
                        )
                        print(product)
                        order_line_item.save()
                    except Product.DoesNotExist:
                        messages.error(request, """One of the products in your bag
                        wasn't found in our database.
                        Please call us for assistance!""")
                        order.delete()
                        return redirect(reverse('view_bag'))
                else:
                    try:
                        subscription = get_object_or_404(Membership, pk=item['item_id'])
                        print(subscription)
                        order_line_item = OrderLineItem(
                            order=order,
                            subscription=subscription,
                            price=subscription.price,
                        )
                        order_line_item.save()
                    except Membership.DoesNotExist:
                        messages.error(request, """One of the products in your bag
                        wasn't found in our database.
                        Please call us for assistance!""")
            return redirect(reverse('checkout_success', args=[order.order_number]))

            # Appoint value if the user wanted to save info
            request.session['save-info'] = 'save-info' in request.POST

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        # Set up Stripe and create Payment Intent
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Create form
        order_form = OrderForm()

        template = 'checkout/checkout.html'

        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle checkout success event
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f"""Order successfully processed!
        Your order number is {order_number}. A confirmation email
        will be sent to {order.email}.""")

    if 'bag' in request.session:
        del request.session['bag']
    if 'subscription_bag' in request.session:
        del request.session['subscription_bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
