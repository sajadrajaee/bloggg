from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login_view, name="login"),
    path('profile/', profile, name="profile"),
    path('edit_profile', edit_profile, name="edit_profile"),
    path('logout/', log_out, name="logout"),
    path('change_password/', change_password, name="change_password"),    
    path('password_reset/', password_reset_request, name="password_reset"),
    path('password_reset_done/', password_reset_done, name="password_reset_done"),
    path('password_reset/<uidb64>/<token>/', password_reset_confirm, name="password_reset_confirm")
]
