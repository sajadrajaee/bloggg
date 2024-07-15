from django.shortcuts import render
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUsers
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def signup(request):
    """sign up page for handling new user accout creation """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            profile_pic = form.cleaned_data['profile_pic']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            password = form.cleaned_data['password1']
            
            if CustomUsers.objects.filter(username=username).exists():
                messages.info(request, "user with this username already exists")
                return redirect('users:signup')
            user = CustomUsers.objects.create(
                    profile_pic = profile_pic,
                    username=username,
                    email=email,
                    gender = gender
                )
            user.set_password(password) #this saves password as hash
            user.save()
            return redirect('users:login')
            #ok! lets send verification email to user
            subject = ''
            message = ''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            #now send mail
            # send_mail(
            #     subject,
            #     message,
            #     email_from,
            #     recipient_list
            # )
        messages.error(request, "invalid form!")
    form = CustomUserCreationForm()
    return render(
        request, 'users/signup.html', {'form':form}
    )
            
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(
                request, 
                username = username,
                password = password
            )
            
            if user is not None:
                login(request, user)
                return redirect('blogapp:home')
            else:
                messages.error(request, "Invalid username or password, try again!")
                return redirect('users:login')
    form = LoginForm()
    return render(request, 'users/login.html', {'form':form})

@login_required(login_url='users:login')
def profile(request):
    return render(request, 'users/profile.html', {})

def edit_profile(request):
    return render(request, 'users/edit_profile.html', {})
