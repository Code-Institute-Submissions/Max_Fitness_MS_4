from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_blog, name='blog'),
    path('<item_id>', views.render_specific_post, name='blog_post'),
    path('update_post/<item_id>', views.update_post, name='update_post'),
    path('delete_post/<item_id>', views.delete_post, name='delete_post'),
    path('add_comment/<item_id>', views.add_comment, name='add_comment'),
]