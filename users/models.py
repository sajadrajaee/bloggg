from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , AbstractUser
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import CustomUserManager

class CustomUsers(AbstractBaseUser, PermissionsMixin):
    profile_pic = models.ImageField(upload_to='users/images') #for profile
    # images_ = models.ImageField() #for posts
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        unique=True,
        validators=[username_validator,],
        max_length=59
    )
    
    email = models.EmailField(max_length=180)
    first_name = models.CharField(max_length=59, blank=True)
    last_name = models.CharField(max_length=59, blank=True)
    
    choices = (
        ('Male', 'male'),
        ('Female', 'female')
    )
    gender = models.CharField(max_length=10, choices=choices)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    # EMAIL_FIELD = ''
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username