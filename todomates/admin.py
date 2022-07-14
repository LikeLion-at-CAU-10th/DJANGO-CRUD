from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Category)
admin.site.register(Todo)

class Todo(admin.TabularInline):
    model = Todo

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        Todo,
    ]

admin.site.register(Category, CategoryAdmin)

