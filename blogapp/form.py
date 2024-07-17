from django import forms
from .models import BlogPost
class PostCreationForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'author',
            'text',
            'images',
        ]
        
        del fields[1]

