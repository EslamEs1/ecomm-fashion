from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin





@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ['author', 'title', 'created']
    search_fields = ['title']

