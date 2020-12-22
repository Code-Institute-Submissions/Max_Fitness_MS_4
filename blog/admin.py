from django.contrib import admin
from .models import BlogPost, BlogComments
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(BlogComments)

