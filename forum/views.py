from django.shortcuts import render
from django.views import generic
from django.views.generic.detail import DetailView
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'forum/forum_page.html'
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    template_name = 'forum/thread.html'