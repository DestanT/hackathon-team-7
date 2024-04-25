from django import forms
from django.forms import ModelForm, Textarea
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'anonymous']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'anonymous': 'Post Anonymously'
        }
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20, 'placeholder': 'Write your post here...'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Comment'
        }
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 3, 'placeholder': 'Write your comment here... please be thoughtful and respectful!'}),
        }