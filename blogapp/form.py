from django import forms
from .models import BlogPost
class PostCreationForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'text']


# class CommentCreationForm(forms.ModelForm):
#     class Meta:
#         model = PostComment
#         fields = '__all__'
        