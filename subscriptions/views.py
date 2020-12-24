from django.shortcuts import render
from .models import Membership
# Create your views here.


def memberships(request):
    memberships = Membership.objects.all()

    context = {
        'memberships': memberships,
    }

    return render(request, 'subscriptions/subscriptions.html', context)
