from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def user_home(request):
    return render(request,'users/user_home.html')

@login_required(login_url='login')
def job(request):
    return render(request,'users/user_home.html')