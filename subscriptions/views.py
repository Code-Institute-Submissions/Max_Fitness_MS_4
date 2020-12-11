from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Membership
# Create your views here.


def memberships(request):
    memberships = Membership.objects.all()

    context = {
        'memberships': memberships,
    }

    return render(request, 'subscriptions/subscriptions.html', context)
