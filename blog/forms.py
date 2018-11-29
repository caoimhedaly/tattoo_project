from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude = ['author', 'views']
    # exclude whichever elements you dont want to display on your form
        