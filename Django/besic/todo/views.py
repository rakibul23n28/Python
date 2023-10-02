from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import TodoItem
from .forms import TodoItemForm

from authentication.decorators import unauthenticated_user,allowed_users,admin_only

# Create your views here.


@login_required(login_url='login')
def user_home(request):
    return render(request,'home/user_home.html')

@login_required(login_url='login')
def todo(request):
    user=request.user
    todos = TodoItem.objects.filter(user=user)
    form = TodoItemForm()
    return render(request, 'todo/todo.html', context={'form': form,'todos':todos})

@login_required(login_url='login')
def add_todo(request):
    user=request.user
    todos = TodoItem.objects.filter(user=user)
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            # Associate the user with the todo item
            todo_item = form.save(commit=False)
            todo_item.user = request.user  # Assuming users are logged in
            todo_item.save()
            return redirect('add_todo')
    else:
        form = TodoItemForm()
    return render(request, 'todo/add_todo.html', context={'form': form,'todos':todos})

def delete_todo(request,id):
    TodoItem.objects.get(pk=id).delete()
    return redirect('todo')

def change_todo(request,id,status):
    todo=TodoItem.objects.get(pk=id)
    todo.completed=bool(status)

    todo.save()
    return redirect('todo')
