from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login_view, name="login"),
    path('profile/', profile, name="profile"),
    path('edit_profile', edit_profile, name="edit_profile"),

]
