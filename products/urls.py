from django.urls import path
from .views import products_page, product_detail

urlpatterns = [
    path('', products_page, name='products'),
    path('<product_id>', product_detail, name='product_detail'),
]
