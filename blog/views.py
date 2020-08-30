from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import post
from django.urls import reverse_lazy


# Create your views here.
class BlogListView(ListView):
    model=post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model=post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogEditView(UpdateView):
    model = post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeltView(DeleteView):
    model = post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class BlogLoggedView(ListView):
    model=post
    template_name = 'success.html'