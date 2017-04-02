from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post


class PostList(ListView):
    model = Post

    template_name = "blog/post_list.html"

    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post

    template_name = 'blog/post_detail.html'

    context_object_name = 'post'
