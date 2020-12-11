from django.urls import path
from .views import memberships

urlpatterns = [
    path('', memberships, name="subscriptions"),
]