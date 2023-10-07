from django.urls import path ,include
from users import views

urlpatterns = [
    path('',views.user_home,name='user_home'),
    path('job/',views.job,name='job'),
    path('todo/',include('todo.urls')),

]