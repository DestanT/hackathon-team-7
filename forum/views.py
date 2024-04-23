from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3
