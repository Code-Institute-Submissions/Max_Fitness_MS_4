from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ Return Bag Page """
    return render(request, "bag/bag.html")
