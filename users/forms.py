from django import forms as formsss
from .models import CustomUsers
from django.contrib.auth import forms

class CustomUserCreationForm(forms.UserCreationForm):
    #this fields will be desplayed in sign up page for users.
    class Meta:
        model = CustomUsers
        fields = (
            'profile_pic', 
            'username', 
            'email' , 
            'gender'
        )
        
class CustomUserChangeForm(forms.UserChangeForm):
    class Meta:
        model = CustomUsers
        fields = (
            'profile_pic',
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'gender'
        )
    
    
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
    
    
class PasswordChangeForm(forms.SetPasswordForm):
    
    class Meta:
        model = CustomUsers
        fields = ['new_password1', 'new_password2']    
        
class PasswordResetForm(forms.PasswordResetForm):
    class Meta:
        model = CustomUsers
        fields = ('email',)
        