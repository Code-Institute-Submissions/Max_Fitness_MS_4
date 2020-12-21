from django.urls import path
from .views import render_blog

urlpatterns = [
    path('', render_blog, name='blog'),
]