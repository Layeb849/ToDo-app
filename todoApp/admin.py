from django.contrib import admin
from .models import CreateTodo
# Register your models here.

class CrateTodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'isComplete', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('isComplete','isDeleted', 'created_at', 'updated_at')

admin.site.register(CreateTodo, CrateTodoAdmin)