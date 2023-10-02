from django.contrib import admin

# Register your models here.
from .models import  Catagory,Item
admin.site.register(Catagory)
admin.site.register(Item)
