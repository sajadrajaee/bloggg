from django import forms as formsss
from .models import CustomUsers
from django.contrib.auth import forms

class CustomUserCreationForm(forms.UserCreationForm):
    class Meta:
        model = CustomUsers
        fields = ('profile_pic', 'username', 'email', 'first_name', 'last_name' )#it may need password option too
        
class CustomUserChangeForm(forms.UserChangeForm):
    class Meta:
        model = CustomUsers
        fields = ('profile_pic','username', 'first_name', 'last_name', 'email')
    
    
class LoginForm(formsss.Form):
    username = formsss.CharField(
        max_length=120, widget=formsss.TextInput(
            attrs={'class': 'myfieldclass'}
        )
    )
    password = formsss.CharField(
        max_length=150, widget=formsss.PasswordInput(
            attrs={'class': 'myfieldclass'}
        )
    )    
# class LoginForm(forms.AuthenticationForm):
    