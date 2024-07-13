from django.contrib import admin
from .models import CustomUsers
from django.contrib.admin import ModelAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUsers

    fieldsets = (
        ('user info', {'fields':('profile_pic','username', 'email', 'first_name', 'last_name', 'password')}),
        ('permissions',{'fields':('is_active', 'is_staff', 'is_superuser', 'groups','user_permissions')})
    )
    
    #things that will apear on create user page
    add_fieldsets = (
        (
            None,
            {
                'fields': (
                    'profile_pic','username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'groups', 'user_permissions'
                )
            }
        ),
    )
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'is_staff'
    ]
    
    list_filter = ('date_joined',)
    
    ordering = ('date_joined',)
    # add_fieldsets = []



admin.site.register(CustomUsers, CustomUserAdmin)
