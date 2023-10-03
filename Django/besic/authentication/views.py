from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .forms import CreateUserForm
from django.contrib import messages
from django.urls import reverse

from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user,allowed_users,admin_only
import uuid  
from django.core.mail import send_mail

from .models import UserActivation
from django.conf import settings
# Create your views here.
@login_required(login_url='login')
@admin_only
def home(request):
    return render(request,'home/home.html')

@login_required(login_url='login')
# @allowed_users(allowed_roles='admin')
def about(request):
    return render(request,'home/about.html')

@login_required(login_url='login')
# @allowed_users(allowed_roles='admin')
def contact(request):
    return render(request,'home/contact.html')

@login_required(login_url='login')
# @allowed_users(allowed_roles='admin')
def items(request):
    return render(request,'home/items.html')

@login_required(login_url='login')
def user_home(request):
    return render(request,'home/user_home.html')

@unauthenticated_user
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login_auth(request,user)
            return redirect('home')
        else:
            messages.info(request,"Username OR Password is incorrect")
    context={}
    return render(request,'home/login.html',context)
    
@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # User is not activated initially
            user.save()

            # Generate a unique activation token
            activation_token = str(uuid.uuid4())

            # Create a user activation instance with the token
            UserActivation.objects.create(user=user, token=activation_token)

            # Send an activation email to the user
            activation_link = request.build_absolute_uri(reverse('activate', kwargs={'token': activation_token}))
            try:
                send_activation_email(user.email, activation_link)
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                messages.success(request, f"Account was created for {user.username}. Check your email to activate the account.")
                return redirect("login")
            except Exception as e:
                user.delete()
                messages.error(request, "An error occurred. Please check your internet and register again.")
                return render(request, 'home/register.html')
    context = {'form': form}
    return render(request, 'home/register.html', context)

def send_activation_email(email, activation_link):
    subject = 'Activate your account'
    message = f'Click the following link to activate your account: {activation_link}'
    from_email = settings.EMAIL_HOST_USER
    to_email = [email]
    send_mail(subject, message, from_email, to_email)


def activate(request, token):
    try:
        activation = UserActivation.objects.get(token=token)
        user = activation.user
        user.is_active = True
        user.save()
        activation.delete()
        messages.success(request, "Your account has been activated.")
    except UserActivation.DoesNotExist:
        messages.error(request, "Invalid activation token.")
    
    return redirect("login")

def logout(request):
    logout_auth(request)
    return redirect('login')


