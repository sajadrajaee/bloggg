from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

app_name = 'blogapp'

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'blogapp/mainpage.html'), name="mainpage"),
    path('list/', posts_list, name='list'),
    path('home/', Home, name="home"),
    path('', allposts, name="posts"),
    path('create/', createpost, name="create"),
    path('about', about, name="about"),
    path('<int:id>/detail/', detailpost, name="detail"),
    path('<int:id>/delete/', delete, name="delete"),
    path('<int:id>/update/', update, name="update"),
    path('search/', search_results, name="search_results"),
    # path('createcomment/', create_comment, name="createcomment"),
    # path('updatecomment/', update_comment, name="updatecomment"),
]