from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

app_name = 'blogapp'

urlpatterns = [
    path('', Home, name="home"), 
    path('mainpage/', mainpage, name="mainpage"),
    path('list/', posts_list, name='list'),
    path('logout/', logout, name="logout"),
    path('create_post/', create_post, name="create_post"),
    path('all_posts/', all_posts, name="all_posts")
]