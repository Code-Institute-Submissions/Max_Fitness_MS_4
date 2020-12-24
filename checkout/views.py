from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
    )
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

# Models
from .models import OrderLineItem, Order
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from subscriptions.models import Membership

# Form
from .forms import OrderForm

# Context function
from bag.contexts import bag_contents

import stripe
import json


# Create your views here.

@require_POST
def cache_checkout_data(request):
    try:
        # Grab session objects
        bag = request.session.get('bag', {})
        subscription_bag = request.session.get('subscription_bag', {})

        # Grabs client_secret and extracts intent id
        pid = request.POST.get('client_secret').split('_secret')[0]

        stripe.api_key = settings.STRIPE_SECRET_KEY

        # .modify is Stripe method used to Update existing Intent
        # .modify also used to update other objects such as Customer and Subs..
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(bag),
            'subscription_bag': json.dumps(subscription_bag),
            'save_info': request.POST.get('save_info'),
            'user': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Handle checkout page and checkout form POST request
    """
    bag = request.session.get('bag', {})
    subscription_bag = request.session.get('subscription_bag', {})

    # Array list of items
    bag_items = []
    if bag:
        for item in bag.items():
            bag_items.append(item)

    if subscription_bag:
        for item in subscription_bag.items():
            bag_items.append(item)

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
    bag_context = bag_contents(request)
    total = bag_context['total']
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
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag_items)
            order.save()

            for item_id, category in bag_items:
                if category != 'membership':
                    try:
                        product = get_object_or_404(Product, pk=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            price=product.price,
                        )
                        order_line_item.save()
                    except Product.DoesNotExist:
                        messages.error(request, """One of the products in your bag
                        wasn't found in our database.
                        Please call us for assistance!""")
                        order.delete()
                        return redirect(reverse('view_bag'))
                else:
                    try:
                        subscription = get_object_or_404(
                            Membership, pk=item_id)
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

            # Appoint value if the user wanted to save info
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
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

        # Attempt to prefill the form with any
        # info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
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

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

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
