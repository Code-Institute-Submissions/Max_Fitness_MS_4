from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Order, OrderLineItem
import json
import time

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from products.models import Product
from subscriptions.models import Membership
from profiles.models import UserProfile


class StripeWH_Handler:
    """Handler Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # Get response intent from the event
        intent = event.data.object

        # Strip intent data intent id, metadata
        pid = intent.id
        bag = json.loads(intent.metadata.bag)
        subscription_bag = json.loads(intent.metadata.subscription_bag)
        save_info = intent.metadata.save_info

        # Unpack json and append it to array
        bag_items = []

        if bag:
            for item in bag.items():
                bag_items.append(item)

        if subscription_bag:
            for item in subscription_bag.items():
                bag_items.append(item)

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        total = round(intent.charges.data[0].amount / 100, 2)

        # Clean the data if field recived is empty
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None


        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.user
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_email = billing_details.email
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    order_total=total,
                    original_bag=json.dumps(bag_items),
                    stripe_pid=pid,
                )
                print(order)
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | \
                        SUCCESS: Verified order already in database',
                    status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=json.dumps(bag_items),
                    stripe_pid=pid,
                )
                for item_id, category in bag_items:
                    if category != 'membership':
                        product = get_object_or_404(Product, pk=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            price=product.price,
                        )
                        order_line_item.save()
                    else:
                        subscription = get_object_or_404(Membership, pk=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            subscription=subscription,
                            price=subscription.price,
                        )
                        order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        self._send_confirmation_email(order)
        # Each time user completes the payment process
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS:\
                Created order in webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """

        # Each time user completes the payment process

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
