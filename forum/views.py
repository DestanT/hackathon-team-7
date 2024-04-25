from django.urls import reverse
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.text import slugify
from .models import Post, Comment, Tag, Topic
from .forms import PostForm, CommentForm, TopicForm

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'forum/forum_page.html'
    context_object_name = 'posts'
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    template_name = 'forum/thread.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.get_object())
        context['tags'] = Tag.objects.filter(posts=self.get_object())
        return context
    

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'forum/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('forum:thread', kwargs={'slug': self.object.slug})


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'anonymous']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.title)
        self.object.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('forum:thread', kwargs={'slug': self.object.slug})


class PostDelete(DeleteView):
    model = Post
    
    def get_success_url(self):
        return reverse('forum:forum')
    

class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('forum:thread', kwargs={'slug': self.kwargs['slug']})
    

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['content']

    def get_success_url(self):
        return reverse('forum:thread', kwargs={'slug': self.object.post.slug})
    

class CommentDelete(DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse('forum:thread', kwargs={'slug': self.object.post.slug})

class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'forums/topic_list.html'

class TopicDetailView(DetailView):
    model = Topic
    slug_field = 'slug'
    template_name = 'forum/topic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.all()
        return context

class TopicCreateView(CreateView):
    model = Topic
    form_class = TopicForm
    template_name = 'forum/create_topic.html'

    def form_valid(self, form):
        topic = form.save(commit=False)
        topic.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forum:topic_detail', kwargs={'slug': self.object.slug})