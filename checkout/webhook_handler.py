from django.http import HttpResponse


class StripeWH_Handler():
    """Handler Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            context=f'Webhook received: {event["type"]}',
            status=200)
