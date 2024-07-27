from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

app_name = 'blogapp'

urlpatterns = [
    path('', Home, name="homepage"), 
    path('mainpage/', mainpage, name="mainpage"),
    path('<int:id>/delete/', delete_post, name="deletepost"),
    path('create_post/', create_post, name="create_post"),
    path('all_posts/', all_posts, name="all_posts"),
    path('<int:id>/update/', update, name="update"),
    path('search/', search_view, name="search"),
    path('<int:id>/detail/', detail_view, name="detail"),
    path('category/', category_post, name="category")
    # path('comment/', comment, name="comment")
]