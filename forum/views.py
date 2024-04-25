from django.views import generic
from django.views.generic.detail import DetailView
from .models import Post, Comment, Tag

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'forum/forum_page.html'
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    template_name = 'forum/thread.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.get_object())
        context['tags'] = Tag.objects.filter(posts=self.get_object())
        return context