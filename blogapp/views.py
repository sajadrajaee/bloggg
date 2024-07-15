from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import BlogPost
from .form import PostCreationForm
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as Logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def posts_list(request):
    titles = BlogPost.objects.all()
    return render(request,'blogapp/posts_list.html',{'titles':titles})

@login_required(login_url='blogapp:mainpage')
def Home(request):

    return render(request, 'blogapp/homepage.html', {})

def mainpage(request):
    return render(request, 'blogapp/mainpage.html', {})

def logout(request):
    Logout(request)
    return redirect('blogapp:mainpage')