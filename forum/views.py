from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import UserPassesTestMixin
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
    template_name = 'forum/post_detail.html'

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
        topic_slug = self.kwargs['topic_slug']
        topic = Topic.objects.get(slug=topic_slug)
        form.instance.topic = topic
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('forum:thread', kwargs={'slug': self.object.slug})


class PostUpdate(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'anonymous']
    template_name = 'forum/edit_post.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('forum:post_list'))

    def get_success_url(self):
        topic_slug = self.object.topic.slug
        return reverse('forum:topic_detail', kwargs={'slug': topic_slug})
    

class PostDelete(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'forum/confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('forum:post_list'))

    def get_success_url(self):
        topic_slug = self.object.topic.slug
        return reverse('forum:topic_detail', kwargs={'slug': topic_slug})

def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('forum:thread', slug=post.slug)
    else:
        form = CommentForm()
    return redirect('forum:thread', slug=post.slug)

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
        context['form'] = PostForm(topic=self.object)
        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, topic=self.object)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = self.object 
            post.save()
            return redirect('forum:topic_detail', slug=self.object.slug)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)

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