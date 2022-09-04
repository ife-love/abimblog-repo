from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PostForm, EditForm
from .models import Post, Category
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ('-created')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
    
    
class AddCategoryView(CreateView):
    model = Category
    fields = "__all__"
    template_name = 'blog/add_category.html'
    


class PostUpdateView(UpdateView):
    model = Post
    form_class  = EditForm
    template_name = 'blog/update_post.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')
    