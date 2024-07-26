from django import forms
from .models import BlogPost, Categories
from django.utils.translation import gettext_lazy as _

class PostCreationForm(forms.ModelForm):
    """ used for creating post by user"""
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'author',
            'text',
            'cate_gory',
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
            'cate_gory',
            'images',
        ]
        
