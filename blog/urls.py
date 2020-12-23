from django.urls import path
from .views import render_blog, render_specific_post, update_post

urlpatterns = [
    path('', render_blog, name='blog'),
    path('<item_id>', render_specific_post, name='blog_post'),
    path('update_post/<item_id>', update_post, name='update_post')
]