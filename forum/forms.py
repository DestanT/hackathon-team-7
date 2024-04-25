from django import forms
from django.forms import ModelForm, Textarea
from .models import Post, Comment, Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'slug', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'placeholder': 'Add your topic description...'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'placeholder': 'Write your post...'}),
        }

    def __init__(self, *args, **kwargs):
        topic = kwargs.pop('topic', None)
        super().__init__(*args, **kwargs)
        if topic:
            self.initial['topic'] = topic

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