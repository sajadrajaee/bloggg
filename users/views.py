from django.shortcuts import render
from .forms import CustomUserCreationForm, LoginForm, CustomUserChangeForm, PasswordChangeForm, PasswordResetForm
from .models import CustomUsers
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail.message import EmailMessage
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.http import Http404
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
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
            #ok! lets send verification email to user
            message = f'Hi mr/ms{user.username}, you have successfully signed up'
            subject = 'email verification'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            #now send mail
            send_mail(
                subject,
                message,
                email_from,
                recipient_list
            )
            return redirect('users:login')
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
                return redirect('blogapp:homepage')
            else:
                messages.error(request, "Invalid username or password, try again!")
                return redirect('users:login')
    form = LoginForm()
    return render(request, 'users/login.html', {'form':form})

def change_password(request):
    if request.method == 'POST': #this post is case senstive using low letter will not send request method
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            subject = 'changed password'
            message = 'Password changed successfully'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.user.email,]
            
            send_mail (
                subject,
                message,
                email_from,
                recipient_list
            )
            return redirect('users:profile')
    form = PasswordChangeForm(user=request.user)
    return render(
        request, 'users/change_password.html', {'form':form}
    )
    
    
# ---------------- PASSWORD FORGOTTEN SECTION --------
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            try:
                user = CustomUsers.objects.get(email=user_email)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                current_site = get_current_site(request)
                reset_url = f"{current_site}/users/password_reset/{uid}/{token}/"
                
                message = render_to_string(
                    'users/password_reset_mail.html', 
                    {
                        'user':user,
                        'reset_url':reset_url,
                    }
                )
                subject = f'email varification'
                email = EmailMessage(
                    subject, message, to=[user_email]
                )
                email.send()
                return redirect('users:password_reset_done')
            except (CustomUsers.DoesNotExist):
                raise Http404("something went wrong or user with this email does not exist!")
            
    form = PasswordResetForm()
    return render(
        request, 'users/password_reset.html', {'form':form}
    )
        
def password_reset_done_mail(request):
    return render(request, 'users/password_reset_mail.html', {})

def password_reset_done(request):
    return render(request, 'users/password_reset_done.html', {})

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUsers.objects.get(pk=uid)
    except (ValueError, OverflowError, CustomUsers.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST': #change password from process
            form = PasswordChangeForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('users:login')
            form.add_error('invalid form, try again!')
        form = PasswordChangeForm(None)
        return render(request, 'users/password_reset_confirm.html', {'form':form})
    return render(
        request, 'users/password_reset_confirm.html', {}
    )
        
    
# ---------------- PROFILE SECTION ---------------
@login_required(login_url='users:login')
def profile(request):
    return render(request, 'users/profile.html', {})

def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(
            request.POST, request.FILES, instance = request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'profile edited succuessfully')
            return redirect('users:profile')
                
        messages.error(request, 'something went wrong, try again!')
        return redirect('users:profile')
    form = CustomUserChangeForm(instance = request.user)
    
    return render(request, 'users/edit_profile.html', {'form':form})

def log_out(request):
    logout(request)
    return redirect('blogapp:mainpage')
