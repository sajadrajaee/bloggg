from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import BlogPost, Categories
from .form import PostCreationForm, UpdateForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as Logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.



# def category_list(request):

#     return render(request, 'blogapp/category.html', )
@login_required(login_url='blogapp:mainpage')
def Home(request):
    items = Categories.objects.all()
    queryset = BlogPost.objects.all().order_by('created_at')
    return render(request, 'blogapp/homepage.html', {'posts':queryset, 'items':items})

def mainpage(request):
    latest = BlogPost.objects.all()[:3]
    return render(request, 'blogapp/mainpage.html', {'latest':latest})

def create_post(request):
    if request.method == 'POST':
        form = PostCreationForm(
            request.POST, request.FILES
        )
        if form.is_valid():
            form.instance.author = request.user #sets logged in user as author of post
            form.save()
            return redirect('blogapp:homepage')
    else:
        form = PostCreationForm(initial={'author': request.user}) 
    return render(request, 'blogapp/post.html', {'form':form})

@login_required(login_url='users:login')
def all_posts(request):
    queryset = BlogPost.objects.filter(author__exact=request.user).order_by('created_at')
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
    return render(request, 'blogapp/update.html', {'form':form, 'message':messages})

def detail_view(request, id):
    try:
        post = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        raise ValueError("something went wrong, Try again!")
    return render(request, 'blogapp/detail.html', {'post':post})    

def search_view(request):

    query = request.GET['query'] #query is the name of html tag here
    posts = BlogPost.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    return render(request, 'blogapp/search.html', {'posts':posts})
    
    
#------------------------- COMMENT ------------------------------

# def comment(request):
#     post = 
#     if request.method == 'POST':
#         form = CommentForm(data=request.POST)
#         if form.is_valid():
#             coment = form.save()
#             coment.post = 
#         raise ValueError("something went wrong, Try again!")
#     form = CommentForm()
#     return render(request, 'blogapp/homepage.html', {'form':form})