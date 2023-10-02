from django.urls import path ,include
from authentication import views

urlpatterns = [
    path('',views.home,name='home'),
    path('user/',include('todo.urls')),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('items/',views.items,name='items'),
]