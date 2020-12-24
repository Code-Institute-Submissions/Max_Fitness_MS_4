from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
    intro = models.CharField(max_length=254, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class BlogComments(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,
                                  related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    body = models.TextField(null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.user.username
