# todo/admin.py
from django.contrib import admin
from .models import TodoItem

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'priority', 'user')
    list_filter = ('completed', 'priority', 'user')
    search_fields = ('title', 'user__username')

admin.site.register(TodoItem, TodoItemAdmin)

