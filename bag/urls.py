from django.urls import path
from .views import view_bag, add_to_bag

urlpatterns = [
    path('', view_bag, name="bag"),
    path('add/<item_id>/', add_to_bag, name="add_to_bag"),

]