from django.urls import path
from .views import view_bag

urlpatterns = [
    path('', view_bag, name="bag"),
]