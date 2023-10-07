from django.urls import path ,include
from todo import views

urlpatterns = [
    path('',views.todo,name='todo'),
    path('add-todo/',views.add_todo,name='add_todo'),
    path('delete-todo/<int:id>/',views.delete_todo,name='delete_todo'),
    path('change-todo/<int:id>/<int:status>/',views.change_todo,name='change_todo'),
]