from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import BlogPost
from .form import PostCreationForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def posts_list(request):
    titles = BlogPost.objects.all()
    return render(request,'blogapp/posts_list.html',{'titles':titles})

@login_required(login_url='users:login')
def Home(request):

    return render(request, 'blogapp/homepage.html', {})

def allposts(request):
    posts = BlogPost.objects.all()
    
    return render (
        request,
        'blogapp/home.html',
        {'posts': posts}
    )

def createpost(request):
    form = PostCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context = {'form':form}
    return render(request, 'blogapp/createpost.html', context)


def about(request):
    return render(request, 'blogapp/about.html')


def detailpost(request, id):
    posts = BlogPost.objects.get(id=id)
    return render(request, 'blogapp/detail.html', {'posts':posts})

def delete(request, id):
    item = BlogPost.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return HttpResponseRedirect('/')
    
    return render(request, 'blogapp/delete.html', {'item':item})

def update(request, id):
    item = BlogPost.objects.get(id=id)
    form = PostCreationForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    
    return render(
        request,
        'blogapp/update.html',
        {
            'form':form
        }
    )


def search_results(request):
    if request.method=='POST':
        query = request.POST['query'] #query : the name of form in html
        results = BlogPost.objects.all().filter(Q(title__icontains=query) | Q(author__icontains=query))
        return render(request, 'blogapp/search_results.html', {'results': results, 'query':query})
    
    else:
        return render(request, 'blogapp/search_results.html', {})



# def login_view(request):
#     username = request.cleaned_data.get['username']
#     password = request.cleaned_data.get['password']
#     user = authenticate(request, username= username, password = password)
#     if user is not None:
#         login(request, user)
#         redirect('blogapp:home')
#     else:
#         return redirect('mainpage')
        

# def create_comment(request):
#     form = CommentCreationForm()
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect('/')
    
#     return render(request, 'blogapp/create_comment.html', {'form':form})

# def update_comment(request, id):
#     object = PostComment.objects.get(id=id)
#     form = CommentCreationForm(request.POST or None, instance=object)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
    
#     return render(
#         request, 'blogapp/update_comment.html', {'form':form}
#     )


# def delete_comment(request, id):
#     pass

# def list_comment():
#     pass
# def detail_comment(request, id):
#     comments = PostComment.objects.all()
#     return render(request, 'blogapp/home.html', {'comments':comments})

