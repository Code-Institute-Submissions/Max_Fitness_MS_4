from django import forms
from .models import BlogPost, BlogComments
from profiles.models import UserProfile


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


class BlogCommentsForm(forms.ModelForm):
    body = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment here !',
            'rows': 4,
            'cols': 50
        }))

    class Meta:
        model = BlogComments
        fields = ('body',)
