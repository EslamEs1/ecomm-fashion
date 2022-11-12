from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView



class PostListView(ListView):
    model = Blog
    context_object_name = 'posts'



class PostDetailView(DetailView):
    model = Blog
    context_object_name = 'post'
