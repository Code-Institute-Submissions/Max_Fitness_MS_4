from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add class to auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'title': 'Blog title',
            'intro': 'Blog post intro',
            'body': 'Blog post content',
            'image_url': 'Blog post image url',
        }

        for field in self.fields:
            self.fields[field].label = False
