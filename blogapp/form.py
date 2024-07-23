from django import forms
from .models import BlogPost


class PostCreationForm(forms.ModelForm):
    """ used for creating post by user"""
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'author',
            'text',
            'images',
        ]        
        del fields[1]
        
class UpdateForm(forms.ModelForm):
    """ updating post for user """
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'text',
            'images',
        ]