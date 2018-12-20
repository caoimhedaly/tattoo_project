from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude = ['author', 'views', 'likes']
        
        widgets = {
            'tags': forms.TextInput(attrs={'data-role': 'tagsinput'}),
        }
    # exclude whichever elements you dont want to display on your form
        