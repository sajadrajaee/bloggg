from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import BlogPost
from .form import PostCreationForm, UpdateForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as Logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

def posts_list(request):
    titles = BlogPost.objects.all()
    return render(request,'blogapp/posts_list.html',{'titles':titles})

@login_required(login_url='blogapp:mainpage')
def Home(request):
    queryset = BlogPost.objects.all().order_by('created_at')
    return render(request, 'blogapp/homepage.html', {'posts':queryset})

def mainpage(request):
    return render(request, 'blogapp/mainpage.html', {})

def create_post(request):
    if request.method == 'POST':
        form = PostCreationForm(
            request.POST, request.FILES
        )
        if form.is_valid():
            #this line of code 
            form.instance.author = request.user
            # form.fields['author'].disabled = True
            form.save()
            return redirect('blogapp:homepage')
    else:
        form = PostCreationForm(initial={'author': request.user}) 
        # del form.fields['author']
    return render(request, 'blogapp/post.html', {'form':form})

@login_required(login_url='users:login')
def all_posts(request):
    queryset = BlogPost.objects.all().order_by('created_at')
        
    return render(request, 'blogapp/all_posts.html', {'posts':queryset})


def delete_post(request, id):
    obj = get_object_or_404(BlogPost, id = id)
    if request.user == obj.author: #it checks that for user to del the post.
        if request.method=='POST':
            obj.delete()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    return render(request, 'blogapp/delete_post.html', {})

def update(request, id):
    
    obj = get_object_or_404(BlogPost, id=id)
    if request.user == obj.author: #it only makes author to edit the post and no one else
        form = UpdateForm(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        messages.error(request, 'sorry! you do not have the permission to customize post.')
        return HttpResponseRedirect('/')
    return render(request, 'blogapp/update.html', {'form':form})
