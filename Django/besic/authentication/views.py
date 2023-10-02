from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user,allowed_users,admin_only

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
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, "Account was created for " + user.username)
            return redirect("login")

    context = {'form': form}
    return render(request, 'home/register.html', context)


def logout(request):
    logout_auth(request)
    return redirect('login')


